#!/usr/bin/env python3
"""test_doc_check.py — the svatantrya doc gate is itself gated.

Hermetic fixtures. Live-endpoint claims are skipped in fixtures (no http
sources used here), so this is fast and offline.
"""
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
CHECKER = HERE.parent / "tools" / "doc_check.py"
GOOD = "# A — x (2026-11-14)\n*Status: CANONICAL. real.*\n\nbody.\n"
REG = {"A.md": {"status": "CANONICAL", "note": "x"}}


def build(root, docs, reg, geo=None):
    (root / "data").mkdir(parents=True)
    (root / "data" / "docs.json").write_text(json.dumps({"format": "svatantrya-docs-registry/1", "docs": reg}))
    (root / "data" / "docs-geometry.json").write_text(json.dumps(geo or {"format": "x", "nodes": [], "edges": []}))
    for n, t in docs.items():
        p = root / n; p.parent.mkdir(parents=True, exist_ok=True); p.write_text(t)


def run(root):
    return subprocess.run([sys.executable, str(CHECKER), "--root", str(root)],
                          capture_output=True, text=True, timeout=60)


class T(unittest.TestCase):
    def test_good_passes(self):
        with tempfile.TemporaryDirectory() as t:
            build(Path(t), {"A.md": GOOD}, REG)
            r = run(Path(t)); self.assertEqual(r.returncode, 0, r.stdout); self.assertIn("SHARP", r.stdout)

    def test_unregistered_fails(self):
        with tempfile.TemporaryDirectory() as t:
            build(Path(t), {"A.md": GOOD, "docs/B.md": "# B\n*Status: REFERENCE. x.*\n"}, REG)
            r = run(Path(t)); self.assertNotEqual(r.returncode, 0); self.assertIn("unregistered doc", r.stdout)

    def test_status_mismatch_fails(self):
        with tempfile.TemporaryDirectory() as t:
            build(Path(t), {"A.md": GOOD.replace("CANONICAL", "REFERENCE")}, REG)
            r = run(Path(t)); self.assertNotEqual(r.returncode, 0); self.assertIn("header status", r.stdout)

    def test_missing_date_fails(self):
        with tempfile.TemporaryDirectory() as t:
            build(Path(t), {"A.md": GOOD.replace(" (2026-11-14)", "")}, REG)
            r = run(Path(t)); self.assertNotEqual(r.returncode, 0); self.assertIn("requires a date", r.stdout)

    def test_dead_link_fails(self):
        with tempfile.TemporaryDirectory() as t:
            build(Path(t), {"A.md": GOOD + "\n[gone](nope.md)\n"}, REG)
            r = run(Path(t)); self.assertNotEqual(r.returncode, 0); self.assertIn("dead link", r.stdout)

    def test_geometry_node_missing_fails(self):
        with tempfile.TemporaryDirectory() as t:
            geo = {"format": "x", "nodes": [{"id": "data/missing.json", "kind": "data"}], "edges": []}
            build(Path(t), {"A.md": GOOD}, REG, geo)
            r = run(Path(t)); self.assertNotEqual(r.returncode, 0); self.assertIn("node missing", r.stdout)


if __name__ == "__main__":
    raise SystemExit(unittest.main())
