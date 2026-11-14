#!/usr/bin/env python3
"""recipes_run.py — executable recipes: how an external agent actually uses
svatantrya.net, tested live, with negative controls.

Each recipe is split into GATHER (live calls → observed dict) and JUDGE (pure
predicate on the observed dict). That separation lets --selftest prove the
judges are not vacuous: every recipe's good observed must PASS, and a set of
deliberate mutations must FAIL. A recipe that cannot be made to fail is not a
test.

  python3 tools/recipes_run.py             # run all recipes live, log report
  python3 tools/recipes_run.py --selftest  # prove every judge bites
  python3 tools/recipes_run.py --json      # print the report JSON

No box access, no key: exactly what ChatGPT/Claude/Google-ADK can reach.
"""
from __future__ import annotations
import copy
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


# ---- GATHER (live) ---------------------------------------------------------
def R1_gather():
    return {"known": (k := mcp_call("openpatala__resolve", {"q": "bodhapancadasika"})),
            "unknown": mcp_call("openpatala__resolve", {"q": "zzzz-not-a-work-qqq"}),
            "known_status": k.get("status"), "known_id": k.get("entity", {}).get("id"),
            "unknown_status": None}


def R1_fix(obs):
    obs["unknown_status"] = obs["unknown"].get("status")
    obs["known_has_no_error"] = "_error" not in obs["known"]
    return obs


def R1_judge(o):
    return (o.get("known_status") == "EXACT" and isinstance(o.get("known_id"), str)
            and len(o.get("known_id") or "") > 0 and o.get("unknown_status") == "NONE"
            and o.get("known_has_no_error") is True)


def R2_gather():
    ev = mcp_call("scholar__passage_evidence",
                  {"work": "bodhapancadasika", "target": "bod-p01-v01"})
    lh = ev.get("layer_sha256") or {}
    rs = ev.get("review_state") or {}
    return {"layers": len(ev.get("layers") or {}), "layer_sha256": len(lh),
            "hashes_valid": bool(lh) and all(isinstance(v, str) and len(v) == 64 for v in lh.values()),
            "review_default": rs.get("default")}


def R2_judge(o):
    return (o.get("layers", 0) >= 1 and o.get("layer_sha256", 0) >= 1
            and o.get("hashes_valid") is True
            and o.get("review_default") in ("UNREVIEWED", "SELF_ATTESTED"))


def R3_gather():
    tr = mcp_call("formal__trace", {"work": "tantrasara-a08", "target": "tsa08-p03"})
    th = (tr.get("formal") or {}).get("theorems") or []
    names = [t.get("theorem") for t in th if isinstance(t, dict)]
    gaps = mcp_call("formal__gaps", {})
    return {"verdict": tr.get("verdict"), "theorems": len(th),
            "named_theorems": sum(1 for n in names if isinstance(n, str) and "::" in n),
            "has_denominator": isinstance(gaps.get("total"), int) and isinstance(gaps.get("gaps"), list)}


def R3_judge(o):
    return (o.get("verdict") == "COMPLETE" and o.get("theorems", 0) >= 1
            and o.get("named_theorems", 0) == o.get("theorems", -1)
            and o.get("has_denominator") is True)


def R4_gather():
    g = mcp_call("formal__gaps", {})
    gl = g.get("gaps")
    return {"coverage": g.get("coverage"), "total": g.get("total"),
            "gap_count": g.get("gap_count"), "returned": g.get("returned"),
            "truncated": g.get("truncated"),
            "gaps_listed": len(gl) if isinstance(gl, list) else None}


def R4_judge(o):
    return (isinstance(o.get("total"), int) and o["total"] > 0
            and isinstance(o.get("coverage"), str) and "/" in o["coverage"]
            and isinstance(o.get("gaps_listed"), int)
            and o["gaps_listed"] == o.get("gap_count")
            and o["gaps_listed"] >= 1)


def R5_gather():
    work, target = "bodhapancadasika", "bod-p01"
    st, body = http_get(f"{SITE}/data/verify/{work}-{target}/manifest.json")
    man = json.loads(body)
    src = next(a for a in man["artifacts"] if a["role"] == "source-bytes")
    lay = next((a for a in man["artifacts"] if str(a.get("role", "")).startswith("layer-")), None)
    st2, art = http_get(f"{SITE}/data/verify/{work}-{target}/{src['name']}")
    got = hashlib.sha256(art).hexdigest()
    obs = {"manifest": st, "artifact": st2, "artifact_bytes": len(art),
           "recorded_sha_len": len(src["sha256"]),
           "recomputed_matches": got == src["sha256"], "sha256": got[:16] + "…"}
    if lay:
        st3, lart = http_get(f"{SITE}/data/verify/{work}-{target}/{lay['name']}")
        obs["layer_artifact"] = st3
        obs["layer_matches"] = hashlib.sha256(lart).hexdigest() == lay["sha256"] and len(lart) > 0
    else:
        obs["layer_artifact"] = None
        obs["layer_matches"] = None
    return obs


def R5_judge(o):
    ok = (o.get("manifest") == 200 and o.get("artifact") == 200
          and o.get("artifact_bytes", 0) > 0 and o.get("recorded_sha_len") == 64
          and o.get("recomputed_matches") is True)
    if o.get("layer_artifact") is not None:
        ok = ok and o.get("layer_artifact") == 200 and o.get("layer_matches") is True
    return ok


def R6_gather():
    ident = mcp_call("openpatala__resolve", {"q": "paramarthasara"})
    ev = mcp_call("scholar__passage_evidence", {"work": "paramarthasara", "target": "param-p04-v29"})
    tr = mcp_call("formal__trace", {"work": "paramarthasara", "target": "param-p04"})
    return {"identity": ident.get("status"), "work_id": ident.get("entity", {}).get("id"),
            "evidence_layers": len(ev.get("layers") or {}),
            "trace": tr.get("verdict"), "identity_hop": (tr.get("identity") or {}).get("status")}


def R6_judge(o):
    return (o.get("identity") == "EXACT" and o.get("work_id") == "paramarthasara"
            and o.get("evidence_layers", 0) >= 1
            and o.get("trace") == "COMPLETE" and o.get("identity_hop") == "BOUND")


def R7_gather():
    bad_tool = mcp_call("no_such_tool_zzz", {})
    bad_target = mcp_call("scholar__passage_evidence",
                          {"work": "bodhapancadasika", "target": "../etc"})
    empty_q = mcp_call("openpatala__resolve", {"q": ""})
    return {"unknown_tool_errored": "_error" in bad_tool,
            "bad_target_errored": "_error" in bad_target,
            "empty_query_status": empty_q.get("status")}


def R7_judge(o):
    return (o.get("unknown_tool_errored") is True
            and o.get("bad_target_errored") is True
            and o.get("empty_query_status") in ("NONE", "INVALID_QUERY"))


def R8_gather():
    ev = mcp_call("scholar__passage_evidence", {"work": "tantrasara-a08", "target": "tsa08-p03"})
    tr = mcp_call("formal__trace", {"work": "tantrasara-a08", "target": "tsa08-p03"})
    withheld = "_error" in ev and "withheld" in (ev.get("_error") or "").lower()
    return {"evidence": "WITHHELD" if withheld else f"{len(ev.get('layers') or {})} layers",
            "evidence_is_honest": withheld or bool(ev.get("layers")),
            "trace": tr.get("verdict"),
            "note": "proof may be COMPLETE while reading is withheld — both stated"}


def R8_judge(o):
    # Honest either way: evidence present, OR explicitly withheld. Trace must be a
    # real verdict. Crucially: a silent empty success (no layers, no withheld) fails.
    return (o.get("evidence_is_honest") is True
            and o.get("trace") in ("COMPLETE", "PARTIAL"))


# Each recipe: (name, purpose, gather, fix, checks, proved, relevance).
# checks = [(label, predicate(observed)->bool)] — named so a failure says WHY.
def R9_gather():
    d = mcp_call("openpatala__search_bibliography", {"q": "tantra", "limit": 3})
    res = d.get("results") or []
    return {"status": d.get("status"), "total": d.get("total"),
            "results": len(res),
            "sha_len": len(d.get("response_sha256") or ""),
            "first_has_id": bool(res) and bool((res[0] or {}).get("work_id"))}


def R10_gather():
    d = mcp_call("treeka__chain", {"work": "tantrasara-a08"})
    ents = d.get("entries") or {}
    shaped = all(isinstance(e, dict) and e.get("work") and e.get("verses")
                 for e in ents.values()) if ents else False
    return {"work": d.get("work"), "rows": d.get("rows"),
            "entries": len(ents), "entries_shaped": shaped}


def R11_gather():
    d = mcp_call("scholar__wheel_level", {"level": 1})
    return {"level": d.get("level"), "has_title": bool(d.get("title")),
            "has_url": bool(d.get("url")), "prompt_len": len(str(d.get("prompt") or "")),
            "has_gate": isinstance(d.get("gate"), dict)}


def R12_gather():
    d = mcp_call("translate__status", {"work": "tantrasara-a08"})
    reg = d.get("registry") or {}
    return {"registry_work": reg.get("work"), "has_status": bool(d.get("STATUS")),
            "registry_verses": reg.get("verses")}


RECIPES = [
    ("R1_identity",
     "Resolve a known work to EXACT+id; an unknown to NONE. Never invent.",
     R1_gather, R1_fix,
     [("known status is EXACT", lambda o: o.get("known_status") == "EXACT"),
      ("known id is a non-empty string", lambda o: isinstance(o.get("known_id"), str) and len(o["known_id"]) > 0),
      ("unknown status is NONE", lambda o: o.get("unknown_status") == "NONE"),
      ("known call carried no error", lambda o: o.get("known_has_no_error") is True)],
     "the resolver distinguishes an exact hit from a miss, and does not fabricate an entity for garbage.",
     "an agent must get a stable work_id before any downstream call; guessing an id poisons every later claim."),

    ("R2_evidence",
     "Passage evidence returns layers + per-layer sha256 + review state.",
     R2_gather, None,
     [("at least one layer", lambda o: o.get("layers", 0) >= 1),
      ("per-layer sha256 present", lambda o: o.get("layer_sha256", 0) >= 1),
      ("every sha256 is 64-hex", lambda o: o.get("hashes_valid") is True),
      ("review default is honest (UNREVIEWED/SELF_ATTESTED)",
       lambda o: o.get("review_default") in ("UNREVIEWED", "SELF_ATTESTED"))],
     "the evidence payload is hash-bearing and its review state is honest by default.",
     "an agent quoting a passage must be able to hand the reader a hash and the real review state, not a claim of review."),

    ("R3_formal",
     "formal__trace -> COMPLETE + named theorems; formal__gaps -> denominator.",
     R3_gather, None,
     [("verdict is COMPLETE", lambda o: o.get("verdict") == "COMPLETE"),
      ("theorems present", lambda o: o.get("theorems", 0) >= 1),
      ("every theorem is named (File :: thm)", lambda o: o.get("named_theorems") == o.get("theorems") and o.get("theorems", 0) >= 1),
      ("gaps carry a denominator", lambda o: o.get("has_denominator") is True)],
     "the formal chain resolves to named, registered Lean theorems, and gaps carry a total.",
     "COMPLETE-with-named-theorems is the difference between 'we checked it' and 'trust us'; an agent must show the names."),

    ("R4_coverage_honesty",
     "Coverage is a fraction; gap_count equals the gaps list (or says truncated).",
     R4_gather, None,
     [("coverage is a fraction", lambda o: isinstance(o.get("coverage"), str) and "/" in o.get("coverage", "")),
      ("total is a positive int", lambda o: isinstance(o.get("total"), int) and o.get("total", 0) > 0),
      ("gap list is non-empty", lambda o: isinstance(o.get("gaps_listed"), int) and o.get("gaps_listed", 0) >= 1),
      ("gap_count is consistent with the list", lambda o: (o.get("gaps_listed") == o.get("gap_count"))
          or (o.get("truncated") is True and o.get("gaps_listed") == o.get("returned")))],
     "coverage is never a bare headline: it carries a denominator and a gap list consistent with gap_count.",
     "the whole estate's honesty depends on never quoting a coverage number without its gap list; this proves the payload can't lie about it."),

    ("R5_outsider_verify",
     "Fetch verify pack + source (and a layer) artifact; recompute sha256.",
     R5_gather, None,
     [("manifest served 200", lambda o: o.get("manifest") == 200),
      ("source artifact served 200", lambda o: o.get("artifact") == 200),
      ("source artifact non-empty", lambda o: o.get("artifact_bytes", 0) > 0),
      ("recorded sha is 64-hex", lambda o: o.get("recorded_sha_len") == 64),
      ("recomputed sha equals recorded", lambda o: o.get("recomputed_matches") is True),
      ("a layer artifact also verifies (if present)",
       lambda o: o.get("layer_artifact") is None
                 or (o.get("layer_artifact") == 200 and o.get("layer_matches") is True))],
     "an outsider recomputes the published bytes' sha256 with no code/account and it matches the recorded hash.",
     "this is the answer to 'how do I know this is real?' — fetch the bytes, sha256sum, compare. If this fails, nothing else is citable."),

    ("R6_research_flow",
     "Chained identity -> evidence (verse) -> proof (chunk), identity BOUND.",
     R6_gather, None,
     [("identity EXACT", lambda o: o.get("identity") == "EXACT"),
      ("work_id is paramarthasara", lambda o: o.get("work_id") == "paramarthasara"),
      ("evidence has layers", lambda o: o.get("evidence_layers", 0) >= 1),
      ("trace COMPLETE", lambda o: o.get("trace") == "COMPLETE"),
      ("trace identity hop BOUND", lambda o: o.get("identity_hop") == "BOUND")],
     "one work carries the whole chain end to end and the trace's identity hop binds to the resolved work.",
     "this is the actual task an agent does: resolve, read, prove, with identity consistent across all three."),

    ("R7_fail_closed",
     "Unknown tool + bad target error; empty query is NONE/INVALID_QUERY.",
     R7_gather, None,
     [("unknown tool errors", lambda o: o.get("unknown_tool_errored") is True),
      ("bad target errors", lambda o: o.get("bad_target_errored") is True),
      ("empty query is NONE/INVALID_QUERY", lambda o: o.get("empty_query_status") in ("NONE", "INVALID_QUERY"))],
     "the surface fails closed: bad input errors, empty input resolves to nothing, never a silent success.",
     "an agent must be able to trust that an empty answer means 'no result', not 'the tool quietly did nothing'."),

    ("R8_honest_boundary",
     "COMPLETE trace may coexist with withheld reading; both stated.",
     R8_gather, None,
     [("evidence is honest (present or explicitly withheld)", lambda o: o.get("evidence_is_honest") is True),
      ("trace returns a real verdict", lambda o: o.get("trace") in ("COMPLETE", "PARTIAL"))],
     "a proof-complete chunk may still withhold its reading, and the surface says which — no silent empty.",
     "prevents an agent from assuming 'proof exists => passage readable' and inventing a reading where none is served."),
    ("R9_bibliography",
     "search_bibliography returns OK + total + results + a response hash.",
     R9_gather, None,
     [("status OK", lambda o: o.get("status") == "OK"),
      ("total is a positive int", lambda o: isinstance(o.get("total"), int) and o.get("total", 0) >= 1),
      ("results returned", lambda o: o.get("results", 0) >= 1),
      ("response_sha256 is 64-hex", lambda o: o.get("sha_len") == 64),
      ("first result carries a work_id", lambda o: o.get("first_has_id") is True)],
     "bibliographic search is real (a query returns ranked works with a stable response hash), not a title-keyword guess.",
     "finding a work by name/alias/identifier is the first half of every research task; the response hash lets a caller cite the exact answer."),

    ("R10_treeka",
     "treeka__chain returns the argument graph rows, each with work+verses.",
     R10_gather, None,
     [("rows >= 1", lambda o: isinstance(o.get("rows"), int) and o.get("rows", 0) >= 1),
      ("entries present", lambda o: o.get("entries", 0) >= 1),
      ("every entry names work+verses", lambda o: o.get("entries_shaped") is True)],
     "the work-to-passages argument graph is assembled and every entry is anchored (work + verse range).",
     "an agent exploring a text needs the passage graph, not isolated chunks; this proves the join exists and is anchored."),

    ("R11_learning",
     "wheel_level returns a teaching level with prompt + gate + url.",
     R11_gather, None,
     [("level echoes 1", lambda o: o.get("level") == 1),
      ("has title", lambda o: o.get("has_title") is True),
      ("has a server-scored gate", lambda o: o.get("has_gate") is True),
      ("prompt is substantive", lambda o: o.get("prompt_len", 0) > 100),
      ("has a source url", lambda o: o.get("has_url") is True)],
     "the learning surface serves a real, gate-bearing level (prompt + scoring rule + source), not a bare form list.",
     "an agent teaching Sanskrit needs the level text AND the server-side gate so a score is never self-reported."),

    ("R12_translation_state",
     "translate__status returns registry state for a work with a status summary.",
     R12_gather, None,
     [("registry work matches", lambda o: o.get("registry_work") == "tantrasara-a08"),
      ("STATUS present", lambda o: o.get("has_status") is True),
      ("registry reports verse count", lambda o: isinstance(o.get("registry_verses"), int))],
     "the translation lane's public read returns the work's registry state honestly (machine-proposed vs gold is in the payload).",
     "an agent must be able to say whether a work is gold or merely machine-proposed before quoting it."),
]


# ---- negative controls: each mutation MUST make at least one check fail ----
MUTATIONS = {
    "R1_identity": [("known_status", "NONE"), ("known_id", ""), ("unknown_status", "EXACT"),
                    ("known_has_no_error", False)],
    "R2_evidence": [("layers", 0), ("layer_sha256", 0), ("hashes_valid", False),
                    ("review_default", "REVIEWED")],
    "R3_formal": [("verdict", "PARTIAL"), ("theorems", 0), ("named_theorems", 0),
                  ("has_denominator", False)],
    "R4_coverage_honesty": [("coverage", "17"), ("total", 0), ("gaps_listed", 0),
                            ("gaps_listed", 5)],
    "R5_outsider_verify": [("manifest", 404), ("artifact", 404), ("artifact_bytes", 0),
                           ("recomputed_matches", False), ("recorded_sha_len", 0)],
    "R6_research_flow": [("identity", "NONE"), ("evidence_layers", 0), ("trace", "PARTIAL"),
                         ("identity_hop", "UNRESOLVED")],
    "R7_fail_closed": [("unknown_tool_errored", False), ("bad_target_errored", False),
                       ("empty_query_status", "EXACT")],
    "R8_honest_boundary": [("evidence_is_honest", False), ("trace", "CORRUPT")],
    "R9_bibliography": [("status", "NONE"), ("total", 0), ("results", 0),
                        ("sha_len", 0), ("first_has_id", False)],
    "R10_treeka": [("rows", 0), ("entries", 0), ("entries_shaped", False)],
    "R11_learning": [("level", 2), ("has_title", False), ("has_gate", False),
                     ("prompt_len", 0), ("has_url", False)],
    "R12_translation_state": [("registry_work", "wrong"), ("has_status", False),
                              ("registry_verses", None)],
}


def _run_checks(checks, obs):
    """Return (ok, [failed labels]). Named so a failure says exactly what broke."""
    failed = [label for label, pred in checks if not pred(obs)]
    return (not failed), failed


def selftest():
    """Prove every recipe is non-vacuous: live observed passes; each mutation fails."""
    fails = []
    for name, _doc, gather, fix, checks, _proved, _rel in RECIPES:
        try:
            obs = gather()
            if fix:
                obs = fix(obs)
        except Exception as e:  # noqa: BLE001
            fails.append(f"{name}: gather crashed: {e}")
            continue
        ok, why = _run_checks(checks, obs)
        if not ok:
            fails.append(f"{name}: live observed FAILED checks {why} (red, not vacuous)")
            continue
        bit, total = 0, len(MUTATIONS.get(name, []))
        for field, badval in MUTATIONS.get(name, []):
            m = copy.deepcopy(obs)
            m[field] = badval
            if _run_checks(checks, m)[0] is False:
                bit += 1
            else:
                fails.append(f"{name}: mutation {field}={badval!r} did NOT flip any check")
        print(f"{'PASS' if bit == total else 'FAIL'} {name}: {bit}/{total} mutations caught (live passes)")
    if fails:
        print("\nSELFTEST FAIL:")
        for f in fails:
            print("  -", f)
        return 1
    print("\nSELFTEST OK: every recipe passes live and rejects all mutations")
    return 0


def main():
    if "--selftest" in sys.argv:
        return selftest()
    as_json = "--json" in sys.argv
    results = []
    for name, doc, gather, fix, checks, proved, relevance in RECIPES:
        try:
            obs = gather()
            if fix:
                obs = fix(obs)
            ok, failed = _run_checks(checks, obs)
        except Exception as e:  # noqa: BLE001 — a crash is a failed recipe
            ok, failed, obs = False, [f"exception: {type(e).__name__}"], {"exception": str(e)[:180]}
        results.append({"recipe": name, "purpose": doc, "proved": proved,
                        "relevance": relevance, "pass": ok,
                        "failed_checks": failed, "observed": obs})
        print(("PASS " if ok else "FAIL ") + name + "  " + doc)
        if not ok:
            print("      failed: " + " | ".join(failed))
            print("      observed: " + json.dumps(obs)[:280])
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
