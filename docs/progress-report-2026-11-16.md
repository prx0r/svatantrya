# PROGRESS REPORT — svatantrya estate docs (2026-11-16)
*Status: HISTORICAL. Timestamped re-verification + drift findings + next plan. (2026-11-16.)*

*Method: full re-read of all 24 docs + data/tools, `git log/status`, `doc_check.py`,
`pytest tools/test_doc_check.py`, `recipes-report.json` archaeology, estate-repo
`git log/status` on box. No live MCP re-probe this pass (read-only); live numbers
below are the 2026-11-14 16:08Z probe unless noted as re-checked 2026-11-16.*

## 1. Where we are

Last session was **2026-11-14**: a docs-culmination sprint, 11 PRs merged in one
day (`#1`–`#11`), HEAD `1badb94` (audit-chain + R13–R16). Tree today is **clean**,
`main` in sync with `origin/main`, no unpushed commits. Local branches for every
merged PR still exist on box (harmless; deletable).

Gate status re-run 2026-11-16 on box:

- `python3 tools/doc_check.py` → `checked 24 docs; 9 live endpoints ok, 0 FAIL,
  0 warn, 0 skip` → **SHARP** (also `--all-warns` clean).
- `pytest tools/test_doc_check.py` → **6 passed**.
- `data/recipes-report.json` → fresh probe **2026-11-16T03:15:25Z, 16/16 PASS**,
  endpoint `https://mcp.svatantrya.net/mcp` (re-run this session; was 2026-11-14).
  R2: 7 layers / 7 sha / `UNREVIEWED`. R4: live coverage string still `17/154`
  with 138 gaps (154 − 138 = 16 — off-by-one persists live).

So: **the culmination record is intact and green. Nothing rotten.**

## 2. What last session delivered (and it holds)

- `PAPER.md`: public paper, all numbers with commands.
- `docs/80-methodical-checklist.md` Step 1: trika-x proven working + two
  independent agent paths (curl + SDK) against two hosts.
- `docs/agent-recipes.md` + `tools/recipes_run.py`: 16 executable recipes,
  every judge with named checks + negative-control mutations, all caught.
- `docs/formal-audit-chain.md`: proving → derivation → construction →
  publication, with honest gaps (essay gates local-only, 10% coverage,
  0 witnesses, 0 DERIVED essays).
- `docs/openpatala-runtime.md`: identity for agents + runtime for
  translation/proof.
- `docs/estate/*` (7 files): per-repo role/gate/honest-state.
- `docs/99-culmination-audit-2026-11-14.md`: DONE/NOT DONE/AT RISK + preservation
  manifest + open-PR register. Still accurate as a snapshot.
- `docs/70-v1-tracker.md`: V1 = engineering complete + live; remainder is owner
  switches + coverage climb.

## 3. Number cross-check (the load-bearing table)

| Claim | Canonical value (docs) | Live probe 2026-11-14 | Verdict |
|---|---|---|---|
| Lean control | 53 PASS / 0 FAIL | n/a (box gate) | CONSISTENT |
| Lean recognition | 26 / 0 | n/a | CONSISTENT |
| EVIDENCE | 206 thm · 155 entries · 2 exempt · 1 gen · 0 prob | n/a | CONSISTENT |
| Full suite | 107 tests OK | n/a | CONSISTENT |
| Traces | 909 (236 COMPLETE / 673 PARTIAL) | n/a | CONSISTENT |
| openpatala | 1034 = 555 + 479 shells · 909 pass · 581 ed · 566 etext · 1559 assert | n/a | CONSISTENT |
| MCP catalog | 115 tools / 8 fam; public 51; console 210; formal 10 | R1–R16 live 16/16 | CONSISTENT |
| Essays | 6, 0 BROKEN, all PARTIAL | essay_derive (box) | CONSISTENT |
| Coverage | **16/154** (30, 60, 70, 99) | **17/154** (R4 observed, 138 gaps, 138 returned) | **DRIFT — see F1** |
| Gaps arithmetic | 154 − 138 = 16 | coverage string says 17 | **OFF-BY-ONE — see F1** |
| Per-layer sha + review_state | V1 tracker: open gap | R2 live: 7 layers, 7 sha, `UNREVIEWED` PASS | **STALE TRACKER — see F2** |
| llms.txt MCP URL | V1 tracker: open gap | estate/svread: names every endpoint (was 0) | **STALE TRACKER — see F2** |

## 4. Findings (3, all small, none load-bearing)

**F1 — coverage 16 vs 17 + gap arithmetic.** `formal-audit-chain.md:130` says
`17/154`; every other canonical doc says `16/154`. The live R4 probe the same
day returned `coverage 17/154, total 154, gap_count 138, returned 138`. But
154 − 138 = 16, so the live string itself is off by one against its own gap
list. Likely cause: a transient +1 on the live host during the recipe run
(trika-x trace churn), plus a typo carried into the audit-chain doc. Fix: keep
canonical at 16/154 until a fresh `formal__gaps` probe confirms otherwise; fix
the audit-chain line + its `allow_stale`.

**F2 — V1 tracker checkboxes stale (good news).** Tracker still lists
per-layer sha + llms-MCP-URL as open, but `estate/svread.md` records both
fixed 2026-11-14 AND recipe R2 proved per-layer sha live (7/7, `UNREVIEWED`).
The tracker was written before the svread repairs landed. Fix: re-probe live,
then flip those two boxes with the probe command cited — do not flip on memory.

**F3 — estate drift since the snapshot (expected, record it).** Box checkouts
have moved after 2026-11-14 23:12Z: trika-x has 4 modified files (docs.json +
3 ipvv traces), svread has 4 modified (app.js + 3 ipvv chain pages), plus
active branches elsewhere (translation-work `tool/validate-layers` + dirty
`GATE.json`, ipvv `box/wheel-gates` + dirty worker, bookfactory/videofactory
auth feat branches). None of this touches `svatantrya/` (clean), but the next
culmination re-verify must re-run the trika-x/svread gates on clean `main`
worktrees — the methodical-checklist already models how (clean-worktree
freshness re-run).

## 5. Plan — what's next and why

**P0 — Re-probe live — DONE 2026-11-16 (16/16 PASS).** Closed F2 both boxes
(per-layer sha + llms MCP URLs verified live; V1 tracker flipped with probe
citations). F1 remains: live says 17/154 vs box/docs 16/154 + gap arithmetic
154−138=16 — queued as box-EVIDENCE decider, not silently promoted.

**P1 — Apply the two one-line doc fixes (10 min, agent).** Why: F1/F2 are
exactly the kind of small inconsistency that erodes trust in a provenance
project. Fix audit-chain 17→16 + docs.json allow_stale; add a dated note to
the V1 tracker pointing at the fresh probe. Keep the culmination audit
untouched (it is a snapshot).

**P2 — Methodical checklist Step 2 (owner picks the lane).** Why: Step 1
proved the pattern (one repo, gates + two agent paths). The highest-value Step
2 is svread (the surface agents actually touch): reader + Scholar + MCP hosts
+ emit_verify refusal test, same shape as Step 1. Alternative Step 2 is
openpatala (identity + restore recipe). Either compounds; ask the owner which.

**P3 — Owner switches in V1-tracker order (owner only).** Why: engineering is
done; the finish is switches, not code. Order by unblock value: token rotation
(SECURITY) → Search Console + indexing confirm → OAuth/directory → Zenodo
first DOI → witness verification → disk reclaim → nightly-green 7-day streak.
No feature creep: R1–R9 stay spec until consent opens R1.

**Explicitly not next:** new recipes, new formal rungs, factory wiring, or
rebuilding the volume. Those are scholarly-coverage and lane work, queued
behind the fresh probe.

## 6. Reproduction commands (run from `/root/svatantrya`)

```sh
git log --oneline -12 --date=short --format='%h %ad %s'
git status --short --branch
python3 tools/doc_check.py --all-warns
python3 -m pytest tools/test_doc_check.py -q
python3 tools/recipes_run.py  # live; rewrites data/recipes-report.json
python3 tools/recipes_run.py --selftest  # judges bite check
```

*Machine proposes, human disposes. BLOCKED is never PASS. Counts carry
denominators or they don't ship.*
