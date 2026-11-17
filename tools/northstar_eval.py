#!/usr/bin/env python3
"""northstar_eval.py — the NORTHSTAR acceptance test, automated (N12/N13/N20).

Runs the four owner turns against a live MCP endpoint and fails closed:

  T1 work status   openpatala__status        one call, denominators, loud absences
  T2 concept       scholar__concept_get      gloss-or-stated-absence + formal anchors
  T3 occurrences   same card                >=3 locators across >=2 works
  T4 related       treeka__chain             rows + no silent empty essays

  python3 tools/northstar_eval.py                 # live, writes data/northstar-report.json
  python3 tools/northstar_eval.py --endpoint URL
  python3 tools/northstar_eval.py --json          # report to stdout only

Exit 0 only if all four turns pass. A failure names the turn and the reason.
"""
from __future__ import annotations

import argparse
import json
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "northstar-report.json"
DEFAULT = "https://mcp.svatantrya.net/mcp"
WORK = "tantrasara-a08"
CONCEPT = "kancuka"


def rpc(endpoint: str, method: str, params: dict, timeout: int = 45) -> dict:
    body = json.dumps({"jsonrpc": "2.0", "id": 1, "method": method,
                       "params": params}).encode()
    req = urllib.request.Request(
        endpoint, data=body,
        headers={"Content-Type": "application/json",
                 "Accept": "application/json, text/event-stream",
                 # Cloudflare 403s the default Python-urllib UA; a named
                 # client UA is required (measured 2026-11-17).
                 "User-Agent": "northstar-eval/1 (+https://svatantrya.net)"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        raw = resp.read().decode("utf-8", "replace")
    for line in raw.splitlines():
        if line.startswith("data: "):
            return json.loads(line[6:])
    return json.loads(raw)


def call(endpoint: str, name: str, args: dict) -> dict:
    out = rpc(endpoint, "tools/call", {"name": name, "arguments": args})
    if "error" in out:
        raise RuntimeError(out["error"])
    result = out.get("result") or {}
    if result.get("isError"):
        raise RuntimeError(result["content"][0]["text"][:300])
    return json.loads(result["content"][0]["text"])


def check(cond, reason: str, failures: list) -> None:
    if not cond:
        failures.append(reason)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--endpoint", default=DEFAULT)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    ep = args.endpoint

    turns = {}

    # --- T1 -----------------------------------------------------------------
    t0 = time.time()
    f1: list = []
    status = call(ep, "openpatala__status", {"work_id": WORK})
    check(status.get("format") == "svatantrya.status/1", "T1: no status format", f1)
    for key in ("identity", "rights", "witnesses", "counts", "formal",
                "traces", "layers", "review_state"):
        check(key in status, f"T1: missing section {key}", f1)
    formal = status.get("formal") or {}
    check("/" in str(formal.get("coverage")), "T1: coverage has no denominator", f1)
    check(formal.get("covered", 0) + len(formal.get("gaps") or [])
          == formal.get("total", -1), "T1: coverage arithmetic inconsistent", f1)
    wit = status.get("witnesses") or {}
    check(wit.get("state") in ("UNPINNED", "RECORDED"),
          "T1: witness state missing", f1)
    check(status.get("review_state") == "UNREVIEWED" or
          bool(status.get("review_state")), "T1: review state missing", f1)
    turns["T1_work_status"] = {"pass": not f1, "failed_checks": f1,
                               "observed": {"work": status.get("work_id"),
                                            "coverage": formal.get("coverage"),
                                            "witnesses": wit.get("count"),
                                            "witness_state": wit.get("state"),
                                            "rights": (status.get("rights") or {}).get("state"),
                                            "traces": (status.get("traces") or {}).get("verdicts")},
                               "seconds": round(time.time() - t0, 2)}

    # --- T2 -----------------------------------------------------------------
    t0 = time.time()
    f2: list = []
    card = call(ep, "scholar__concept_get", {"term": CONCEPT})
    check(card.get("id") == CONCEPT, "T2: concept id mismatch", f2)
    check("gloss_state" in card, "T2: gloss state absent", f2)
    check(card.get("gloss_state") == "CURATED" or bool(card.get("warning")),
          "T2: missing gloss was not stated", f2)
    check(bool(card.get("formal_anchors")), "T2: no formal anchor", f2)
    check(card.get("tier") in ("T", "R"), "T2: no tier", f2)
    check("scope_note" in card, "T2: no scope note", f2)
    check(card.get("review_state") == "UNREVIEWED", "T2: review state not stated", f2)
    turns["T2_concept"] = {"pass": not f2, "failed_checks": f2,
                           "observed": {"id": card.get("id"),
                                        "gloss_state": card.get("gloss_state"),
                                        "tier": card.get("tier"),
                                        "anchors": [a.get("theorem") for a in (card.get("formal_anchors") or [])]},
                           "seconds": round(time.time() - t0, 2)}

    # --- T3 -----------------------------------------------------------------
    t0 = time.time()
    f3: list = []
    occ = card.get("occurrences") or []
    works = sorted({o.get("work") for o in occ if o.get("work")})
    check(len(occ) >= 3, f"T3: only {len(occ)} occurrences returned", f3)
    check(len(works) >= 2, f"T3: occurrences span {len(works)} work(s)", f3)
    check(all(o.get("verse_id") for o in occ), "T3: occurrence without verse_id", f3)
    check("occurrence_note" in card, "T3: no note that hits are tokens", f3)
    turns["T3_occurrences"] = {"pass": not f3, "failed_checks": f3,
                               "observed": {"count": len(occ), "works": works,
                                            "sample": occ[:3]},
                               "seconds": round(time.time() - t0, 2)}

    # --- T4 -----------------------------------------------------------------
    t0 = time.time()
    f4: list = []
    chain = call(ep, "treeka__chain", {"work": WORK})
    entries = chain.get("entries") or {}
    check(chain.get("rows", 0) > 0, "T4: no treeka rows", f4)
    silent = [k for k, v in entries.items()
              if isinstance(v, dict) and v.get("essays") == []
              and not v.get("essays_note")]
    check(not silent, f"T4: silent empty essays on {silent[:3]}", f4)
    noformal = [k for k, v in entries.items()
                if isinstance(v, dict) and v.get("formal_reference") is False
                and not v.get("formal_note")]
    check(not noformal, f"T4: unformalised rows without note: {noformal[:3]}", f4)
    turns["T4_related"] = {"pass": not f4, "failed_checks": f4,
                           "observed": {"rows": chain.get("rows"),
                                        "counts": chain.get("counts")},
                           "seconds": round(time.time() - t0, 2)}

    passed = sum(1 for t in turns.values() if t["pass"])
    report = {
        "format": "svatantrya.northstar-eval/1",
        "northstar": "NORTHSTAR-2026-11-17.md",
        "checked_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "endpoint": ep,
        "work": WORK,
        "concept": CONCEPT,
        "passed": passed,
        "total": 4,
        "turns": turns,
        "verdict": "OPERATIONAL" if passed == 4 else "NOT_OPERATIONAL",
    }
    if args.json:
        print(json.dumps(report, indent=1, ensure_ascii=False))
    else:
        OUT.parent.mkdir(parents=True, exist_ok=True)
        OUT.write_text(json.dumps(report, indent=1, ensure_ascii=False) + "\n",
                       encoding="utf-8")
        print(f"{report['verdict']}: {passed}/4 turns — {OUT}")
        for name, t in turns.items():
            print(f"  {'PASS' if t['pass'] else 'FAIL'} {name} "
                  f"({t['seconds']}s)" + ("" if t["pass"] else f" :: {t['failed_checks']}"))
    return 0 if passed == 4 else 1


if __name__ == "__main__":
    raise SystemExit(main())
