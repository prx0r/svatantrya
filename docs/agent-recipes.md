# AGENT RECIPES — tested sequences for real work

*Status: CANONICAL. Eight recipes an external agent actually runs against the
public surface (no key, no box). Every one is executable and was run live on
2026-11-14 — see `data/recipes-report.json` (8/8). Run them yourself:
`python3 tools/recipes_run.py`.*

Each recipe states purpose, the exact calls, the expected shape, and the
honesty rule. The runner (`tools/recipes_run.py`) logs observed values so a
result is interpretable, not a vibe.

---

## R1 — Identity: resolve, never invent

**Purpose:** turn a name into a stable `work_id`, and admit when there isn't one.

```
openpatala__resolve {"q":"bodhapancadasika"}   → {"status":"EXACT","entity":{"id":"bodhapancadasika",...}}
openpatala__resolve {"q":"zzzz-not-a-work-qqq"} → {"status":"NONE", ...}
```
**Expected:** known → `EXACT` + `entity.id`; unknown → `NONE` (never a fabricated entity).
**Rule:** `CANDIDATES`/`NONE` = draft-only downstream. Never substitute a title string for an id.

## R2 — Evidence: layers with verifiable hashes

**Purpose:** read a passage with per-layer content, hashes, and review state.

```
scholar__passage_evidence {"work":"bodhapancadasika","target":"bod-p01-v01"}
→ {layers:{t1,l0,argmap,l2,c1,l3,l4,c2}, layer_sha256:{...}, stack_sha256, review_state:{default:"UNREVIEWED"}, projection_sha256}
```
**Expected:** ≥1 layer, every `layer_sha256` a 64-hex digest, `review_state.default` in {`UNREVIEWED`,`SELF_ATTESTED`}.
**Rule:** a hash proves *identity*, not *correctness*. `UNREVIEWED` is the honest default — report it.

## R3 — Proof: the formal chain

**Purpose:** get the machine-checked chain and the coverage denominator.

```
formal__trace {"work":"tantrasara-a08","target":"tsa08-p03"}
→ {verdict:"COMPLETE", formal:{theorems:[...named Lean theorems...]}, identity:{status:"BOUND"}, verdict_scope:...}
formal__gaps {}
→ {coverage:"17/154", total:154, gap_count:138, gaps:[...]}
```
**Expected:** `COMPLETE` + named theorems; gaps carry a denominator.
**Rule:** `COMPLETE` means *links present*, not "the translation is correct or reviewed". Read `verdict_scope`.

## R4 — Coverage honesty: a fraction, never a bare number

```
formal__gaps {} → coverage "17/154", total 154, gaps[] non-empty
```
**Rule:** never report coverage without its denominator and gap list.

## R5 — Outsider verification (the killer recipe)

**Purpose:** prove the whole chain is checkable with only fetch + sha256.

```
GET /data/verify/bodhapancadasika-bod-p01/manifest.json   → artifacts[{role:"source-bytes", sha256, name}]
GET /data/verify/bodhapancadasika-bod-p01/source.txt        → bytes
sha256(bytes) == manifest artifact sha256                   → TRUE
```
**Expected:** manifest 200, artifact 200, recomputed hash equals the recorded one.
**Rule:** this is the one an agent should cite when asked "how do I know this is real?" — no code, no account, no trust in us.

## R6 — Full research flow (identity → evidence → proof)

**Purpose:** the canonical chain on a work that carries all three.

```
openpatala__resolve {"q":"paramarthasara"}                      → EXACT, work_id
scholar__passage_evidence {"work":"paramarthasara","target":"param-p04-v29"}  → 7 layers
formal__trace {"work":"paramarthasara","target":"param-p04"}   → COMPLETE, identity BOUND
```
**Expected:** all three succeed and the trace's `identity` hop is `BOUND`.
**Rule:** read at verse scope (`…-v29`), prove at chunk scope (`param-p04`) — same chunk, two granularities.

## R8 — Honest boundary (proof ≠ readable evidence)

**Purpose:** do not assume a COMPLETE trace implies the passage is readable.

```
scholar__passage_evidence {"work":"tantrasara-a08","target":"tsa08-p03"}  → ToolError: "Passage unavailable or withheld"
formal__trace          {"work":"tantrasara-a08","target":"tsa08-p03"}  → verdict COMPLETE (links present)
```
**Expected:** evidence explicitly withheld/unavailable, trace may still be COMPLETE.
**Rule:** report both states. A withheld reading is data, not an error to paper over.

## R7 — Fail-closed: nothing fakes success

```
scholar__passage_evidence {"work":"bodhapancadasika","target":"../etc"}  → ToolError (bad target)
no_such_tool_zzz {}                                                       → "unknown tool" error
```
**Rule:** errors are clean and explicit; a call never returns an empty success where truth runs out.

---

## The pattern behind all eight

**resolve identity → read evidence (with hashes + review state) → check proof →
report gaps → verify bytes.** Every step answers honestly: `NONE`, `UNREVIEWED`,
`WITHHELD`, `PARTIAL`, `UNPINNED` are valid answers and must be reported as such.
The runner logs the observed value beside every PASS/FAIL, so a run is a record,
not an opinion.
