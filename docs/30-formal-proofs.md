# 30 — Formal proofs (formal-trika Lean spine)

Lean's `decide` is the first estate component that **proves** instead of
scoring. Heuristic PASS is advisory; a checked theorem plus a refused mutant is
a fact about a finite model. This is the proof-carrying spine everything hangs
off: peer review → teacher → practice consume only gated outputs.

## What is machine-checked (all green, 2026-11-14, Lean 4.34.1)

| Harness | Result | Command |
|---|---|---|
| Control (`control/run.sh`) | **53 PASS / 0 FAIL** | positives + hand-written must-fail twins |
| Recognition (`recognition/run.sh`) | **26 passed / 0 failed** | same discipline |
| EVIDENCE registry | **206 theorems · 155 entries · 2 exemptions · 1 generated · 0 problems** | `tools/evidence_check.py` |
| Coverage | **16/154 chunks (10%)**, gap list published | same |
| TABLE readings | **rc=0** | `tools/table.py --check` |
| Axiom audit | **CLEAN (static)** — no sorry/axiom/native_decide | `tools/axiom_audit.py --check` |
| Full suite | **107 tests OK** | `python3 -m unittest discover -s formal-trika/tests` |

## The 206 vs 155 story (read this before citing counts)

49 of the 206 are the generated `PrakriyaSlice.lean` certificate slice. They are
**not** EVIDENCE rows and **not** passage coverage: they prove structural
well-formedness of 44 DERIVED traces under a **bound receipt** (file+pack sha256,
Lean version, exit 0) — `PrakriyaSlice.receipt.json`. `evidence_check` treats
generated files fail-closed: receipt missing, exit≠0, or sha mismatch →
PROBLEM. Tamper test: receipt `exit_code→1` produced 1 problem; restored → 0.
Coverage stays honestly **16/154**.

## What a rung is (the discipline every theorem follows)

**prereg → model → must-fail twin → EVIDENCE → TABLE → run receipt.** No
exceptions. The twin is the anti-vacuity check: if the checker were vacuous,
the mutant would compile — so each mutant is verified to *refuse* at the exact
named proposition. Twins are single-definition diffs; the harness enforces
exactly-one-error.

## Traces (the moat)

909 trace bundles (236 COMPLETE / 673 PARTIAL, every PARTIAL naming its gaps)
compile every ledger locator to source bytes + layer hashes + proof hops +
formal theorems + citing essays. `trace_bundle.py --verify` re-runs every hash
against the live files; any byte change fails with the first divergence named.
An outsider verifies with `curl` + `sha256sum` and nothing else.

## The treeka view

`treeka_report.py` renders the gap report: unargued / cruxless / essayless /
unformalised per work, plus the rung queue (phr mala → VBT clusters → tsa08
remainder). Live over MCP as `treeka__chain` / `treeka__frontier`.

## Limits (stated, not hidden)

- `decide` proves only inside its finite scope. A KEY row is a count-fact, not
  a proof of textual entailment; registry refs are associations, not verdicts.
- Heuristic PASS, beautiful output, and big models are never treated as proof.
- Coverage is 10% and published with its denominator. Never reported as "done".
