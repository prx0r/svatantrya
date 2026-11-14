# OPENPATALA AS RUNTIME — identity for agents, spine for translation

*Status: CANONICAL. openpatala's two concrete jobs: (1) the MCP identity
surface agents call, (2) the runtime identity store that translation, formal
proof, and the reader all key on. Verified 2026-11-14.*

openpatala is not a translation tool and not a proof tool. It is the **runtime
that says which work/edition/passage everything else is about**, and it answers
that over MCP so ChatGPT, Google-style agents, and scholars can use the same
authority the pipelines use.

## 1. For agents — the identity root (ChatGPT, Google ADK, scholars)

Any MCP client calls 8 read tools (full contract in openpatala
`MCP-FOR-AGENTS.md`; also federated as `openpatala__*` on
`https://mcp.svatantrya.net/mcp`):

| Ask | Tool | Result |
|---|---|---|
| "which work is this?" | `resolve {q}` | `EXACT`+`work_id` / `CANDIDATES` / `NONE` |
| "the full dossier?" | `get_bundle {entity_id}` | editions, etexts, passages, assertions |
| "search the catalogue" | `search_bibliography {q,…}` | ranked works + `response_sha256` |
| "what facets exist?" | `bibliography_facets` | recorded types/traditions/providers/languages |
| "what's unbridged?" | `get_frontier` | coverage frontier |
| "is it live?" | `get_health` | works, passages, witnesses counts |

**The one rule for agents:** keep the `work_id` **and** a locator (`tsa08-p03`)
downstream; never substitute a title. `NONE`/`CANDIDATES` mean draft-only.

## 2. For translation — the runtime the layer pipeline keys on

translation-work's `passages.jsonl` locators equal the DB's
`passages.citation_value` (verified by trika-x `bridge_resolve.py --check`).
So the identity store is the join table between:
- the Sanskrit work/edition/etext rows (what bytes exist), and
- the translation layers per chunk (what has been said about them).

Nothing in translation-work invents an id; it borrows openpatala's. A changed
edition label invalidates downstream approval (recorded, never auto-healed).

## 3. For proof — what trika-x reads

trika-x `bridge_resolve.py` maps a chunk locator → the DB's work/edition/etext
rows and writes them into the trace bundle's `identity` hop. It records
`witness: UNPINNED` and `status: UNRESOLVED` where the DB has none — it never
invents an edition or witness. (See `docs/formal-audit-chain.md`.)

## 4. For scholars — the honest state, not a marketing number

`check.py` is GREEN with **2 recorded BLOCKED** that are stated, not hidden:
- adapters discover nothing (upstream data gap);
- **witnesses = 0** corpus-wide — a printed edition is not a witness; the
  resolver enforces `UNPINNED` rather than invent a siglum.
Counts: **1034 works** (555 enriched + 479 Muktabodha identity shells, the
shells have rights NULL and are not publishable), 909 passages, 1559
assertions, 121 translations, 20 people.

## 5. Why it comes together (the organism question, scoped down)

The estate composes as a **fixed assembly line**, not a self-modifying
organism: openpatala (identity) → translation-work (layers) → trika-x (proof +
trace) → svread (surface) → factories (render), with humans at the sign-off and
publish gates. Growth is the **scholarly coverage queue** and new preregistered
Lean rungs — not agents autonomously rewriting the graph. Multiple agents may
*read* the whole surface; *writes* are lane-owned and human-gated. That keeps it
open-source without making "who has authority" a per-request question: there is
exactly one authority model — humans publish, machines propose.

## 6. Verify it yourself

- openpatala `MCP-FOR-AGENTS.md` + `python3 tools/mcp_acceptance_run.py` (8/8).
- svatantrya `docs/agent-recipes.md` R1 (resolve), R9 (bibliography), R10
  (treeka), R12 (translation state) — all live-tested with negative controls.
- Identity→proof join: recipe R6 (`resolve` → `formal__trace`, identity BOUND).
