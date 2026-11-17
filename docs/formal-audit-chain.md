# FORMAL AUDIT CHAIN — proving, derivation, construction, publication

*Status: CANONICAL. The concrete method by which Sanskrit becomes a checkable
result: bytes → layers → Lean theorem → trace → essay → publication. Every step
names its gate and whether it is exposed over MCP or local-only. Verified
2026-11-14.*

This is the answer to: *how is Lean used, how is Sanskrit proved, how does
Sanskrit become an essay, and how is the chain audited end to end?*

---

## 0. The chain, one line per hop

```
source bytes ──► translation layers ──► Lean theorem ──► trace bundle ──► essay ──► publication
  (openpatala)     (translation-work)     (trika-x)        (trika-x)      (scholar)   (owner)
   sha256           sha per layer          decide+twins     one JSON      claims +    DOI / site
```

Each hop carries **bytes + hash + status + where to re-fetch**. A hop that cannot
name its input fails closed. `UNKNOWN`, `UNPINNED`, `CANDIDATE`, `PARTIAL` are
valid states; none is silently promoted.

---

## 1. Proving — how Lean is used

Lean is used **only to prove finite structural facts**, never doctrine. A rung is:

1. **prereg** (dated file) — the exact finite claim, kill conditions, tier R.
2. **model** (`control/<Name>.lean`) — inductive types + a `def` table + a
   `theorem ... := by decide`. Example (`Kancuka.lean`): five coverings as an
   `inductive`, a `restricts : Kancuka → Capacity` table, then
   `pairings_distinct : ((kancukas.map restricts).eraseDups).length = 5 := by decide`.
3. **must-fail twin** (`Broken<Name>.lean`) — one definition corrupted; the
   *same* statement must now fail at the same `by decide`. `must_fail.py` accepts
   the mutant only if Lean reports exactly one error, at that line, saying the
   proposition is false. This is the anti-vacuity check: if the checker were
   vacuous, the twin would compile.
4. **EVIDENCE row** — `{theorem, kind, chunks:[{locator, tier, status, via}]}`.
   The theorem names the passage locators it rests on.
5. **harness receipt** — `runs/runs.jsonl`: Lean version, exit code per harness,
   git rev. A proof without a receipt is not counted.
6. **TABLE reading** — plain-English scope note per theorem, so its limit is
   stated ("counts the ARGMAP roster, not the whole text").

**What Lean proves:** the finite model (counts, orderings, gatings) and that the
checker bites (the twin refuses). **What it does NOT prove:** that the Sanskrit
*means* this — that is a human/tier judgement recorded in EVIDENCE and the
reading, never inferred from `decide`.

**Exposed over MCP (public):** `formal__evidence` (tier/kind/chunks),
`formal__runs` (receipts+exit codes+Lean version), `formal__axioms` (static
CLEAN: no `sorry`/axiom/native_decide), `formal__table` (scope notes).

## 2. Derivation — how Sanskrit is bound to the proof

`trace_bundle.py` compiles one `trika-trace/1` bundle per chunk with separated
hops (each measured independently, never inferred from another):

| Hop | Carries | Status vocabulary |
|---|---|---|
| source | bytes sha256 + edition + witness | BOUND / UNKNOWN / FAIL; witness `UNPINNED` |
| identity | openpatala rows (work/edition/etext) | RESOLVED / `UNRESOLVED` |
| layers | per-song t1/l0/argmap/l2/c1/l3/l4/c2 hashes | present / UNKNOWN |
| proofs | `chunk_gate` from GATE.json | PASS / `BLOCKED` / UNKNOWN |
| formal | EVIDENCE theorems citing the locator | `REGISTERED` (run_bound:false) |
| essays | essays whose text names the locator | verbatim mention only |

`verdict = COMPLETE` means **links present** — not correct, not reviewed. The
`assurance` block scores each dimension separately. So "Sanskrit is being proved"
is operationalised as: *this chunk's theorem registry row (tier T/R) cites this
locator, and the bundle re-hashes the bytes it came from.*

**Exposed:** `formal__trace {work,target}` → the whole bundle. `formal__bridge
{chunk}` → the identity rows.

## 3. Construction — how Sanskrit becomes an essay

The essay is a **rendering of the chain**, never a free composition. Locally
(trika-x, not on the public MCP) the method is:

1. **compile** (`essay_compile.py`) — essays are compiled data: each claim has a
   `verse_id`, a tier, and links to a chunk. Never hand-written prose first.
2. **gate** (`essay_check.py`) — validates the triple `.md/.essay.json/.receipt`;
   every tiered bullet must link a claim AND every claim be cited; `[CLM-id]`
   must name a real claim; **T claims bind an exact span** to the current ledger
   passage, its digest and edition label; exit 0 = `READY_FOR_HUMAN_REVIEW` (a
   human gate, not approval, not publication).
3. **derive** (`essay_derive.py`) — the northstar gate: for every essay claim,
   walk claim → chunk → trace → EVIDENCE → openpatala block. Verdicts:
   **DERIVED** (green end to end) / **PARTIAL** (a hop is CANDIDATE/PARTIAL) /
   **BROKEN** (a hop is missing). Currently 6 essays, all PARTIAL, 0 BROKEN —
   honest: none is fully DERIVED yet (the Q12 DERIVED-exemplar gate is open).
4. **pushback** (`pushback.py`) — cross-model destroy pass over a draft; a
   report, never an edit, never a verdict.

**Exposed:** the *inputs* are public (`formal__trace`, `scholar__passage_evidence`);
the essay compile/gate/derive tools are **local-only** (they read the whole
corpus and write receipts). An external agent can verify an essay's claims by
calling `formal__trace` on each cited chunk — the recipe R16 does exactly this.

## 4. Publication — the human gate

Nothing auto-publishes. The path: READY_FOR_HUMAN_REVIEW → a human signs →
svread `emit_verify.py` publishes the exact bytes the trace hashes (refuses on
any mismatch) → optional Zenodo DOI. `publication: NOT_AUTHORIZED` is the
default state on every claim page until a human acts.

## 5. The audit chain, end to end (what an outsider can check)

For any published chunk, an outsider recomputes the whole chain with no code:

1. `formal__trace` → verdict + theorem names + source `bytes_sha256`.
2. fetch the verify pack (`/data/verify/<work>-<target>/`) → `source.txt`.
3. `sha256sum source.txt` → equals the bundle's recorded hash (recipe R5).
4. `formal__evidence <theorem>` → tier + the chunk it cites (recipe R13).
5. `formal__runs` / `formal__axioms` → receipts + no-sorry (recipes R14/R15).

That is the "proven method": each step is a command, each output is hash-pinned,
and the test recipes (`docs/agent-recipes.md`) execute the whole set live with
negative controls, so the method itself is tested, not asserted.

## 6. Honest gaps (stated, not hidden)

- **Essay compile/gate/derive are not on MCP** — an agent can verify essay claims
  via `formal__trace` but cannot run `essay_derive` remotely. Exposing it would
  need a new svread tool wrapping trika-x's local gate (a lane decision).
- **Coverage is 16/154 chunks** — proof exists for a fraction; the gap list is
  published and the queue is worked in order.
- **Witnesses are 0** — the chain proves identity + structure, never a
  manuscript; source hop says `UNPINNED`.
- **No essay is DERIVED yet** — all 6 are PARTIAL; the DERIVED exemplar (Q12)
  is the gate before any DOI.

## 7. What we deliberately do NOT build (scope)

An "autonomous agentic organism" with multi-agent write authority, reputation,
and self-growth is **out of scope** — it is over-engineering for the concrete
problem. The foundation is: *prove (Lean), derive (trace), construct (essay
gates), publish (human)*. Multiple agents may *read* the surface freely; writes
are human-gated and lane-owned. Growth comes from the scholarly coverage queue
and new preregistered rungs, not from agent autonomy loops.
