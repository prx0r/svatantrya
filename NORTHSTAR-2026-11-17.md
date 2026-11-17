# NORTHSTAR — one system: ask about a work, ask what a term is, follow it everywhere
*Status: CANONICAL. Owner verbatim vision + acceptance test + 20-item build queue. (2026-11-17.)*

*This file is the product target. Nothing else is. Until the acceptance test at
§3 passes cold, twice, on the public internet, every session starts by reading
this file and ends by reporting which N-item moved.*

---

## 1. Owner verbatim (never edit; quote in place)

> oh right openpatala is the main usecase here with this.. like the idea here is i ask chatgpt about a  work and it browses openpatala and tells me the exact status , in the same breath i can ask what is a kankun aand it has the trika-x formalisation, then links to where that appears in all these passage s and related points, essays.. ALL ONE SYSTEM.

---

## 2. Interpretation (kept separate from the words)

Four questions, one conversation, one system, one breath apart:

1. **"What's the status of <work>?"** → openpatala answers with the exact state:
   identity, edition, witness count, rights, layer/review state, formal coverage,
   trace verdicts. Not prose — a status object with denominators.
2. **"What is a kañcuka?"** → a concept card: plain definition, tier, and the
   trika-x formalisation that anchors it (theorem ids, scope note, what is *not*
   proved).
3. **"Where does it appear?"** → every passage across every work that carries the
   term, each with locator + layer status + gate state.
4. **"Related points, essays."** → treeka chain, ref-links, essays that discuss
   it, each with its derive verdict and its gaps named.

**ALL ONE SYSTEM.**

### What "one system" means, concretely

- The same work id resolves across all four answers. No re-guessing titles.
- The concept card and the passages come from the same closed world.
- Citations resolve; unresolved things say `UNPINNED` / `UNREVIEWED` / `PARTIAL`
  out loud instead of disappearing.
- A stranger with a ChatGPT account and no API key can do all four.

### What it does not mean

- It does not mean the machine interprets. Tiers stay separate.
- It does not mean coverage is high. Today the formal layer covers 16/154
  passages; the answer must carry that denominator.
- It does not mean a concept is "defined by AI". Concepts resolve to attested
  forms + tiered evidence, or they resolve to nothing.

---

## 3. Acceptance test (the definition of operational)

**Cold start.** Fresh ChatGPT session, web-connected, no account beyond ChatGPT,
no box access, no prior context. The user types only the four questions below.
Every expected field must appear, and every citation must resolve.

| Turn | User says | Must come back |
|---|---|---|
| T1 | "What is the status of tantrasara-a08?" | work id + EXACT match, edition count, witness count (0 → `UNPINNED`), rights, review state, layer count, formal coverage with denominator, trace verdict with COMPLETE/PARTIAL reason |
| T2 | "What is a kañcuka?" | concept card: definition, tier (T/R), the five names, formal anchors (`AnswerKey.lean :: key_five_kancukas`, `Kancuka.lean :: count_5`, `pairings_distinct`), and the explicit scope note ("finite table only; not doctrine") |
| T3 | "Where does that appear?" | ≥3 passage locators across ≥2 works, each with layer status + gate; no invented locators |
| T4 | "Related points and essays" | treeka chain nodes, ≥1 essay with derive verdict and named gaps, related concepts |

**Pass condition:** all four turns in one session, no dead end, no invented id,
no unlabelled claim. Latency: each turn answers within the connector's step
budget (target p95 ≤ 15s, single tool call per turn where possible).

**Fail conditions (any one = not operational):** a turn needs a tool the model
cannot discover; a status number lacks its denominator; a concept has no formal
anchor and no honest `UNPINNED`; a passage locator does not resolve; the model
must guess a work id.

**Run twice, on two different days, with two different front-end models.**
First run proves it works; second run proves it was not luck.

### 3a. Baseline measured 2026-11-17 (N1 — done)

Every line below was produced by a call to `https://mcp.svatantrya.net/mcp`
this session, no auth. This is the starting score, not an estimate.

| Turn | Observed today | Verdict |
|---|---|---|
| T1 | `openpatala__resolve {q:"tantrasara-a08"}` → `EXACT`, id `tantrasara-a08`, edition 1, **witness 0**, etext 1, translation 1 | works, but **no rights, no review, no coverage, no trace verdict in the same call** |
| T2 | no concept tool exists. `formal__evidence {theorem:"key_five_kancukas"}` → `found:false`; only `{theorem:"AnswerKey.lean :: key_five_kancukas"}` → `found:true`, tier T, chunk tsa08-p03. `scholar__search_texts` → **281 raw results, no card** | **fails the turn** |
| T3 | semantic search returns passages, but there is **no term→occurrence index**; same concept query gives no stable locus list | **fails the turn** |
| T4 | `treeka__chain {work:"tantrasara-a08"}` → 4 rows, nodes 17, cruxes 2, `formal_refs` present; but `essays: []` for tsa08-p01/p02 (global `essayless: 331`) | partial: chain yes, essays **silently empty** |

Also recorded: `openpatala__resolve` takes `q`, not `query` — a schema detail a
model handles but a human script must know. Global treeka counts today:
909 passages, 578 unargued, 123 cruxless, 331 essayless, 893 with no formal
reference.

**Baseline score: T1 partial, T2 fail, T3 fail, T4 partial. Zero of four turns
is cleanly operational.** That is the honest starting line.

---

## 4. What exists today vs what is missing (measured 2026-11-17)

Live public surface: `https://mcp.svatantrya.net/mcp`, 51 tools, no auth.

| Piece | State | Evidence |
|---|---|---|
| Work resolution + status primitives | **EXISTS** | `openpatala__resolve` → EXACT + dossier fields (edition/witness/etext/translation counts) |
| Passage evidence with layer hashes | **EXISTS** | `scholar__passage_evidence` → 7 layers, 7 sha, `UNREVIEWED` |
| Formal chain per passage | **EXISTS** | `formal__trace tantrasara-a08/tsa08-p03` → COMPLETE, 9 theorem rows |
| Formal evidence by theorem | **BROKEN for humans** | `formal__evidence {"theorem":"key_five_kancukas"}` → `found:false`; needs `AnswerKey.lean :: key_five_kancukas` |
| Concept lookup ("what is a kañcuka") | **MISSING** | no concept entity; `scholar__search_texts` returns 281 raw passages, no card |
| Term → occurrences across works | **MISSING** | no term index; only semantic search |
| One-call status object for a work | **MISSING** | fields are spread across `resolve` + `get_bibliography_dossier` + `translate__status` + `formal__trace` |
| Related points / essays by concept | **PARTIAL** | `treeka__chain`, `scholar__ref_links` exist but are id-driven, not concept-driven |
| ChatGPT instructions for this workflow | **MISSING** | initialize instructions describe families, not the 4-turn recipe |
| Cold-start eval for this workflow | **MISSING** | 16/16 recipes test tools, not the conversation |

**Known numeric defect to fix before T1 can be trusted:**
`formal__gaps` reports `covered:17, total:154, gap_count:138` — 17+138=155.
Cause: `formal-trika/tools/federation_gateway.py` counts the work-level ref
`vbt` as a covered passage. True value is 16/154. Fix = intersect `covered`
with `all_chunks` before counting.

---

## 5. The 20-item build queue (work top to bottom; no creep)

| # | Item | Done when |
|---|---|---|
| N1 | Record the cold-start baseline | the 4 turns are run by hand and each observed output is written down as of today |
| N2 | Define the **Status Object** schema | one JSON shape: identity, rights, witness, layers, review, trace verdict, coverage+gaps, provenance commands |
| N3 | Add `openpatala__status` (one call) | returns the Status Object for a work id, no second call needed |
| N4 | Build the **concept index** | stable concept ids + Sanskrit surface forms (kañcuka, tattva, śaktipāta, …) with tier |
| N5 | Add `concept__get` | returns definition + formal anchors + occurrences + essays + related, in one call |
| N6 | Fix `formal__evidence` | accepts a bare theorem name; returns the entry or an honest `near_matches` |
| N7 | Build term→occurrence index | concept id → passage locators across works, each with gate + layer status |
| N8 | Concept-first search | `scholar__search_texts` returns the concept card first, passages second |
| N9 | Related-points join | concept → ref_links/treeka → essays, deduped, tiered, gaps named |
| N10 | One orchestration call | `estate__ask` (or equivalent) so ChatGPT does the join in one step, not four calls that can time out |
| N11 | Publish the 4-turn script | exact prompts in plugin instructions + `llms.txt` + a user one-pager |
| N12 | Cold-start eval harness | automated: runs T1–T4 against the live public MCP, asserts required fields, fails closed |
| N13 | Wire eval into CI + nightly | new recipe family R-NS1..R-NS4; drift becomes a dated finding |
| N14 | Fix the coverage over-count | gateway intersects `covered` with `all_chunks`; live says 16/154 and 138 gaps consistently |
| N15 | Loud absences | Status Object prints `witnesses: 0 → UNPINNED` and `rights: NULL → UNPUBLISHABLE`, never omits them |
| N16 | Review state on every claim | `review_state` + signer (or `UNREVIEWED`) present in Status Object and concept card |
| N17 | Essay linkage with verdicts | every returned essay carries PARTIAL/DERIVED plus its named gaps; no silent empty list |
| N18 | Latency budget | measure the 4-turn p95; if over budget, fold the joins into fewer calls |
| N19 | User-facing one-pager | "ask ChatGPT these four things", with real captured outputs, live on the site |
| N20 | Regression loop | every session re-runs the acceptance test; NORTHSTAR stays the checklist; not "done" until twice cold |

---

## 6. Laws that still apply

- **Machine proposes, human disposes.** No auto-sign, no auto-publish, no DOI.
- **BLOCKED ≠ PASS.** A missing link is stated with its reason.
- **DERIVED ≠ truth.** Machine traces are computation, not scholarship.
- **Counts carry denominators or they do not ship.**
- **Private stays private.** The diary lane never enters this workflow without
  explicit, scoped, revocable consent.

---

## 7. Progress log (append-only; this is the checklist in motion)

### 2026-11-17 — first autonomous pass

Acceptance test after this pass: **4/4 OPERATIONAL** (`tools/northstar_eval.py`,
report in `data/northstar-report.json`). Latency measured inside the same run:
T1 1.37s · T2 0.24s · T3 shares T2's call · T4 1.53s.

| # | State | What landed |
|---|---|---|
| N1 | DONE | baseline measured and recorded in §3a |
| N2 | DONE | Status Object schema `svatantrya.status/1` |
| N3 | DONE | `openpatala__status` live: identity, rights, witnesses, counts, formal, traces+blocked gates, layers, review, provenance |
| N4 | DONE | `svread/tools/emit_concepts.py` → 415 concept ids |
| N5 | DONE | `scholar__concept_get` live one-call card |
| N6 | DONE | `formal__evidence` accepts bare theorem names (fail-closed on ambiguity) |
| N7 | DONE | 345 concepts carry occurrences; kañcuka = 6 across 4 works |
| N8 | PARTIAL | `scholar__concept_search` returns concepts before passages; `search_texts` itself unchanged |
| N9 | DONE (light) | concept card resolves `related_concepts`; essays stay in treeka |
| N10 | DEFERRED | measured need is 3 calls at ~1.5s p95 — no orchestration tool until a client shows a tighter step budget |
| N11 | DONE | live bundle instructions carry the four-turn order |
| N12 | DONE | `tools/northstar_eval.py`, fails closed |
| N13 | DONE | wired into `.github/workflows/checks.yml` |
| N14 | DONE | live `formal__gaps` → 16/154, 138 gaps, covered+gaps=total |
| N15 | DONE | witnesses 0 → UNPINNED, rights NULL → not publishable, both in one call |
| N16 | DONE | `review_state: UNREVIEWED` on status and concept cards |
| N17 | DONE | `treeka__chain` annotates empty essays and unformalised rows |
| N18 | DONE | 4-turn p95 = 1.53s (well inside budget) |
| N19 | DONE | `docs/northstar-user-guide.md` |
| N20 | ACTIVE | eval runs every session; not "done" until it passes cold twice, on two models |

**Honest remaining gap:** T1's "exact status" is exact about identity, rights,
witnesses and traces. It does not yet say which *edition* is the base text
(`editions[0]` exists in the dossier but the status object surfaces counts, not
the edition title/URI). That is the next real hole, not a cosmetic one.

**Three drift numbers fixed while here:** live coverage now 16/154 (was 17/154
self-contradictory); `PAPER.md` mutant count corrected to 57 (was inflated to
79); the suite count corrected to 132 (was stated as 107) in PAPER, 30, 60 and
80. Historical docs (99) left untouched as snapshots.

---

*One system: the work, the word, the occurrences, the arguments, the essays.
If a stranger cannot do all four in one sitting, it is not finished.*
