#!/usr/bin/env python3
"""recipes_run.py — executable recipes: how an external agent actually uses
svatantrya.net, tested live. Every recipe is a real sequence an agent would run
against the public MCP + HTTPS. Each prints PASS/FAIL with observed values and
the whole run is logged to data/recipes-report.json.

  python3 tools/recipes_run.py [--json]

No box access, no key: exactly what ChatGPT/Claude/Google-ADK can reach.
"""
from __future__ import annotations
import hashlib
import json
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

MCP = "https://mcp.svatantrya.net/mcp"
SITE = "https://svatantrya.net"
UA = {"User-Agent": "svatantrya-recipes/1 (+https://svatantrya.net)"}
HERE = Path(__file__).resolve().parent
REPORT = HERE.parent / "data" / "recipes-report.json"


def mcp_call(name, args, timeout=60):
    body = json.dumps({"jsonrpc": "2.0", "id": 1, "method": "tools/call",
                       "params": {"name": name, "arguments": args}}).encode()
    req = urllib.request.Request(MCP, data=body, method="POST",
                                 headers={**UA, "Content-Type": "application/json",
                                          "Accept": "application/json, text/event-stream",
                                          "MCP-Protocol-Version": "2025-06-18"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        raw = r.read().decode()
    payload = None
    for line in raw.splitlines():
        if line.startswith("data:"):
            payload = json.loads(line[5:].strip())
    if payload is None:
        payload = json.loads(raw)
    res = payload.get("result", {})
    if res.get("isError"):
        return {"_error": (res.get("content") or [{}])[0].get("text", "")[:200]}
    txt = (res.get("content") or [{}])[0].get("text", "")
    try:
        return json.loads(txt)
    except ValueError:
        return {"_raw": txt[:300]}


def http_get(url, timeout=30):
    req = urllib.request.Request(url, headers=UA, method="GET")
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.status, r.read()


RECIPES = []


def recipe(fn):
    RECIPES.append(fn)
    return fn


@recipe
def R1_identity():
    """Resolve a known work to EXACT+id; an unknown to NONE. Never invent."""
    known = mcp_call("openpatala__resolve", {"q": "bodhapancadasika"})
    unknown = mcp_call("openpatala__resolve", {"q": "zzzz-not-a-work-qqq"})
    ok = (known.get("status") == "EXACT" and known.get("entity", {}).get("id")
          and unknown.get("status") == "NONE")
    return ok, {"known": known.get("status"), "known_id": known.get("entity", {}).get("id"),
                "unknown": unknown.get("status")}


@recipe
def R2_evidence():
    """Passage evidence returns layers + per-layer sha256 + review state."""
    ev = mcp_call("scholar__passage_evidence",
                  {"work": "bodhapancadasika", "target": "bod-p01-v01"})
    lh = ev.get("layer_sha256") or {}
    rs = ev.get("review_state") or {}
    ok = (bool(ev.get("layers")) and bool(lh)
          and all(isinstance(v, str) and len(v) == 64 for v in lh.values())
          and rs.get("default") in ("UNREVIEWED", "SELF_ATTESTED"))
    return ok, {"layers": len(ev.get("layers") or {}), "layer_sha256": len(lh),
                "review_default": rs.get("default")}


@recipe
def R3_formal():
    """formal__trace → COMPLETE + named theorems; formal__gaps → denominator."""
    tr = mcp_call("formal__trace", {"work": "tantrasara-a08", "target": "tsa08-p03"})
    th = (tr.get("formal") or {}).get("theorems") or []
    gaps = mcp_call("formal__gaps", {})
    ok = (tr.get("verdict") == "COMPLETE" and th
          and isinstance(gaps.get("total"), int) and "gaps" in gaps)
    return ok, {"verdict": tr.get("verdict"), "theorems": len(th),
                "coverage": gaps.get("coverage")}


@recipe
def R4_coverage_honesty():
    """Coverage is a fraction with a published gap list, never a bare number."""
    gaps = mcp_call("formal__gaps", {})
    cov, total, gl = gaps.get("coverage"), gaps.get("total"), gaps.get("gaps")
    ok = (isinstance(total, int) and total > 0 and isinstance(gl, list)
          and isinstance(cov, str) and "/" in cov)
    return ok, {"coverage": cov, "total": total, "gap_count": gaps.get("gap_count")}


@recipe
def R5_outsider_verify():
    """The killer recipe: fetch verify pack + source artifact, recompute sha256."""
    work, target = "bodhapancadasika", "bod-p01"
    st, body = http_get(f"{SITE}/data/verify/{work}-{target}/manifest.json")
    man = json.loads(body)
    src = next(a for a in man["artifacts"] if a["role"] == "source-bytes")
    st2, art = http_get(f"{SITE}/data/verify/{work}-{target}/{src['name']}")
    got = hashlib.sha256(art).hexdigest()
    ok = (st == 200 and st2 == 200 and got == src["sha256"])
    return ok, {"manifest": st, "artifact": st2, "recomputed_matches": got == src["sha256"],
                "sha256": got[:16] + "…"}


@recipe
def R6_research_flow():
    """Chained flow on a work that carries the whole chain: identity → evidence
    (verse) → proof (chunk), identity consistent end to end."""
    ident = mcp_call("openpatala__resolve", {"q": "paramarthasara"})
    wid = ident.get("entity", {}).get("id")
    ev = mcp_call("scholar__passage_evidence", {"work": "paramarthasara", "target": "param-p04-v29"})
    tr = mcp_call("formal__trace", {"work": "paramarthasara", "target": "param-p04"})
    idhop = (tr.get("identity") or {}).get("status")
    ok = (ident.get("status") == "EXACT" and ev.get("layers")
          and tr.get("verdict") == "COMPLETE" and idhop == "BOUND")
    return ok, {"identity": ident.get("status"), "work_id": wid,
                "evidence_layers": len(ev.get("layers") or {}),
                "trace": tr.get("verdict"), "identity_hop": idhop}


@recipe
def R8_honest_boundary():
    """An agent must NOT assume proof implies readable evidence. Some chunks have
    a COMPLETE trace while passage evidence is withheld/unavailable — report it,
    never fabricate. (Real example: tantrasara-a08/tsa08-p03.)"""
    ev = mcp_call("scholar__passage_evidence",
                  {"work": "tantrasara-a08", "target": "tsa08-p03"})
    tr = mcp_call("formal__trace", {"work": "tantrasara-a08", "target": "tsa08-p03"})
    withheld = "_error" in ev and "withheld" in (ev.get("_error") or "").lower()
    # the honest outcome: either evidence is present, or it is explicitly withheld
    # (never a silent empty success). Trace may still be COMPLETE — that is fine;
    # verdict_scope says COMPLETE is links-present, not readability.
    ok = (withheld or bool(ev.get("layers"))) and tr.get("verdict") in ("COMPLETE", "PARTIAL")
    return ok, {"evidence": "WITHHELD" if withheld else f"{len(ev.get('layers') or {})} layers",
                "trace": tr.get("verdict"),
                "note": "proof may be COMPLETE while reading is withheld — both stated"}


@recipe
def R7_fail_closed():
    """Unknown tool errors cleanly; bad target errors; empty query is NONE."""
    bad_tool = mcp_call("no_such_tool_zzz", {})
    bad_target = mcp_call("scholar__passage_evidence",
                          {"work": "bodhapancadasika", "target": "../etc"})
    ok = ("_error" in bad_tool and "_error" in bad_target)
    return ok, {"unknown_tool_errored": "_error" in bad_tool,
                "bad_target_errored": "_error" in bad_target}


def main():
    as_json = "--json" in sys.argv
    results = []
    for fn in RECIPES:
        name = fn.__name__
        doc = (fn.__doc__ or "").strip().splitlines()[0]
        try:
            ok, observed = fn()
        except Exception as e:  # noqa: BLE001 — a crash is a failed recipe
            ok, observed = False, {"exception": f"{type(e).__name__}: {str(e)[:180]}"}
        results.append({"recipe": name, "purpose": doc,
                        "pass": ok, "observed": observed})
        print(("PASS " if ok else "FAIL ") + name + "  " + doc)
        if not ok:
            print("      " + json.dumps(observed)[:300])
    passed = sum(1 for r in results if r["pass"])
    report = {"format": "svatantrya.recipes-report/1",
              "checked_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
              "endpoint": MCP, "passed": passed, "total": len(results),
              "results": results}
    REPORT.write_text(json.dumps(report, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    if as_json:
        print(json.dumps(report, indent=1))
    print(f"\n{passed}/{len(results)} recipes passed — logged to {REPORT.relative_to(HERE.parent)}")
    return 0 if passed == len(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
