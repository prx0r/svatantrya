#!/usr/bin/env python3
"""doc_check.py — svatantrya documentation gate.

svatantrya is the clean public documentation home, so its gate checks
documentation integrity first and live endpoints second (no box DB needed):

  - every *.md under root and docs/ is registered in data/docs.json;
  - header `*Status: TIER*` (first 15 lines) matches the registry;
  - CANONICAL / HISTORICAL / SUPERSEDED docs carry a YYYY-MM-DD;
  - every relative markdown link resolves;
  - geometry nodes/edges resolve;
  - live-endpoint claims (`http_status`) must return the expected code
    (SKIP loudly when the network is unreachable — never a silent pass).

  python3 tools/doc_check.py [--root REPO] [--all-warns]

Exit 0 + "docs: SHARP" iff zero FAIL.
"""
from __future__ import annotations
import json
import os
import re
import sys
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
WARN_PATS = [re.compile(r"\b\d{2,5}\s+(?:works|theorems|tools|passages|chunks|"
                        r"tests|bundles|entries|witnesses|certificates|songs)\b"),
             re.compile(r"(?<!\d)\d{1,5}/\d{1,5}(?!\d)")]
UA = {"User-Agent": "svatantrya-doc-gate/1"}


def http_status(url, timeout=15):
    try:
        req = urllib.request.Request(url, headers=UA, method="GET")
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status
    except urllib.error.HTTPError as e:
        return e.code
    except Exception:  # noqa: BLE001 — network down => None (skip)
        return None


def main() -> int:
    root = Path(sys.argv[sys.argv.index("--root") + 1]) if "--root" in sys.argv else REPO
    show_all = "--all-warns" in sys.argv
    reg = json.loads((root / "data" / "docs.json").read_text(encoding="utf-8"))
    docs = reg["docs"]
    fails, warns, skips, live_checked = [], [], [], 0
    on_disk = {str(p.relative_to(root)) for p in
               list(root.glob("*.md")) + list((root / "docs").rglob("*.md"))}
    for f in sorted(on_disk):
        if f not in docs:
            fails.append(f"unregistered doc: {f}")
    for name, spec in docs.items():
        p = root / name
        if not p.is_file():
            fails.append(f"registered but missing: {name}")
            continue
        text = p.read_text(encoding="utf-8", errors="replace")
        head = "\n".join(text.split("\n")[:15])
        m = re.search(r"\*Status:\s*([A-Z_]+)", head)
        if not m or m.group(1) != spec["status"]:
            fails.append(f"{name}: header status {m.group(1) if m else None!r} != registry {spec['status']!r}")
            continue
        if spec["status"] in ("CANONICAL", "HISTORICAL", "SUPERSEDED"):
            if not (re.search(r"\d{4}-\d{2}-\d{2}", head) or re.search(r"\d{4}-\d{2}-\d{2}", name)):
                fails.append(f"{name}: {spec['status']} requires a date")
        for claim in spec.get("claims", []):
            if "http_status" in claim:
                code = http_status(claim["http_status"])
                if code is None:
                    skips.append(f"{name}:{claim['id']} skipped: network unreachable")
                elif code != claim.get("expect", 200):
                    fails.append(f"{name}:{claim['id']} {claim['http_status']} → {code} (want {claim.get('expect', 200)})")
                else:
                    live_checked += 1
        if spec["status"] == "CANONICAL":
            allows = [re.compile(a) for a in spec.get("allow_stale", [])]
            for wp in WARN_PATS:
                for wm in wp.finditer(text):
                    ls = text.rfind("\n", 0, wm.start()) + 1
                    le = text.find("\n", wm.end()); le = len(text) if le == -1 else le
                    pn = text.rfind("\n", 0, max(0, ls - 1)); nn = text.find("\n", le + 1)
                    window = text[pn + 1:(len(text) if nn == -1 else (text.find("\n", nn + 1) if text.find("\n", nn + 1) != -1 else len(text)))]
                    if re.search(r"\d{4}-\d{2}-\d{2}", window):
                        continue
                    ctx = text[max(0, wm.start() - 50):wm.end() + 20].replace("\n", " ")
                    if not any(a.search(ctx) for a in allows):
                        warns.append(f"{name}: unregistered live-looking number {wm.group(0)!r}")
        for lm in re.finditer(r"\[[^\]]*\]\(([^)#\s][^)\s]*)\)", text):
            tgt = lm.group(1).split("#", 1)[0]
            if not tgt or tgt.startswith(("http://", "https://", "mailto:")) or "@" in tgt:
                continue
            if not ((root / tgt).exists() or (p.parent / tgt).exists()):
                fails.append(f"{name}: dead link → {tgt}")
    try:
        geo = json.loads((root / "data" / "docs-geometry.json").read_text(encoding="utf-8"))
    except (OSError, ValueError) as e:
        fails.append(f"geometry unreadable: {e}"); geo = {"nodes": [], "edges": []}
    ids = {n["id"] for n in geo.get("nodes", [])}
    for n in geo.get("nodes", []):
        k = n.get("kind")
        if k in ("doc", "code", "data") and not (root / n["id"]).is_file():
            fails.append(f"geometry: {k} node missing: {n['id']}")
        elif k == "repo" and not os.path.isdir(f"/root/{n['id']}"):
            skips.append(f"geometry: repo absent on box (skipped): {n['id']}")
    for e in geo.get("edges", []):
        for end in (e.get("from"), e.get("to")):
            if end not in ids and end not in docs:
                fails.append(f"geometry: edge endpoint unknown: {end}")
    print(f"checked {len(docs)} docs; {live_checked} live endpoints ok, "
          f"{len(fails)} FAIL, {len(warns)} warn, {len(skips)} skip")
    for s in skips:
        print("  SKIP:", s)
    for w in (warns if show_all else warns[:10]):
        print("  WARN:", w)
    if not show_all and len(warns) > 10:
        print(f"  … {len(warns) - 10} more warnings (--all-warns)")
    for f in fails:
        print("  FAIL:", f)
    print("docs: " + ("DRIFT" if fails else "SHARP"))
    return 1 if fails else 0


if __name__ == "__main__":
    raise SystemExit(main())
