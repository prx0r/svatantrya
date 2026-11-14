# AGENTS INDEX — one map for any agent using the estate
*Status: CANONICAL. Agent entry point: the one correct path from question to checkable answer. (2026-11-14.)*

## The one-sentence model

**Identity → evidence → proof → surface.** openpatala says *which text*;
translation-work holds the *layers*; trika-x *proves* structure and compiles the
trace; svread *shows* it. Each hop carries bytes + hash + status; a hop that
cannot name its input fails closed.

## Entry points (live, no key for reads)

| Need | Endpoint / tool |
|---|---|
| One public MCP for everything | `https://mcp.svatantrya.net/mcp` (~51 tools, no auth) |
| Identity only | `openpatala__resolve {q}` → `EXACT`/`CANDIDATES`/`NONE` + `work_id` |
| Verified passage + layers | `scholar__passage_evidence {work, target}` → layers + per-layer sha + review state |
| Formal chain | `formal__trace {work, target}` → verdict COMPLETE/PARTIAL + Lean theorems |
| Coverage / gaps | `formal__gaps {}` → covered/total + gap list |
| Owner console (all tools) | `https://mcp.sanskrit.help/mcp` (bearer) |

## The correct order (and why)

1. **Resolve identity first.** `openpatala__resolve`. If it returns
   `CANDIDATES`/`NONE`, everything downstream is draft-only — say so, do not
   guess an id. Pass `work_id` **and** a locator downstream; never a title.
2. **Read evidence.** `scholar__passage_evidence`. Use `layer_sha256` +
   `review_state`. `UNREVIEWED` is the honest default; report it.
3. **Check proof.** `formal__trace`. `COMPLETE` means the links are present —
   **not** that the translation is correct or reviewed. Read `verdict_scope`.
4. **Show gaps.** `formal__gaps` when claiming coverage. Never a numerator
   without its denominator.

## What to never do (and why it matters)

- **Never invent Sanskrit, a witness, an edition, or a DOI.** The record says
  `UNPINNED`/`BLOCKED`/`UNKNOWN`; repeat it.
- **Never present a fork as settled.** Meaning-forks live in the literal-gloss
  layer; show them as forks.
- **Never treat a hash as quality.** Hashes prove *identity*, not
  *correctness*. The three stamps stay separate: bytes, mechanics, meaning.
- **Never write.** Writes answer `-32001` (OAuth unissued). Publication,
  promotion, sign-off are human-only, always.

## How to verify what you were told

- Run `trika-x` `formal-trika/tools/chatgpt_acceptance_run.py` (raw mode,
  16/16) or the connected-mode suite (T16–T20) — it checks the whole public
  surface with live calls and reports PASS/FAIL with observed values.
- Every number in this estate's CANONICAL docs is gate-verified
  (`trika-x`/`openpatala`/`svatantrya` each carry a `doc_check`). If a doc's
  number is stale, its gate is red — fix the number, never the gate.

## Reading map (deep dives)

| Topic | Doc |
|---|---|
| The thesis, laws, tiers | `00-thesis.md` |
| Identity root (openpatala) | `10-openpatala.md` |
| Evidence (translation layers) | `20-translation-evidence.md` |
| Proof (Lean, traces) | `30-formal-proofs.md` |
| One MCP surface | `40-federation-mcp.md` |
| Endgame recipes (diary→media) | `50-recipes.md` |
| Live state, verified | `60-live-state.md` |
| Per-repo reference | `estate/*.md` |
| Glossary | `90-glossary.md` |

## The trust contract in one line

*Machine proposes, human disposes. BLOCKED is never PASS. A count carries its
denominator, and every claim resolves to source bytes or says why not.*
