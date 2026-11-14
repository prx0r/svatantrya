# 20 — Translation evidence (translation-work + Scholar)

Translation-work is the **evidence** layer: T1→L0→ARGMAP→L2→C1→C2→L3→L4, per
chunk, sha-pinned per layer, with ARGMAP nodes feeding the crux queue and
treeka. Trika-x reads its layer bytes and writes nothing back; Scholar
(svread + translation-work) is the review/signoff surface.

## The layers (public names first; machine keys still work)

| Key | Public name | What it is |
|---|---|---|
| T1 | draft-translation | Lore-primed fast pass: verse draft + quick gloss per token. Coverage before sharpness. |
| L0 | literal-gloss | Term-by-term scholarly audit: every genuine meaning-fork as a ranked option with grammatical grounds. Forks live HERE and nowhere else. |
| ARGMAP | argument-map | What the verse says as a whole: speaker, question, premises, inference, payoff, uncertainties. Adjudicates L0 forks on the record. |
| L2 | reading-translation | Our translation proper: readable line-by-line English, every clause tracing to literal-gloss ids. |
| C1 | essence | The subtle essence: the sharpest poetic reading of what the verse DOES. |
| C2 | register-render | A register rendering (eli5/genz/poetic/formal) over essence + final: style plus reproducing prompt/model/date/paragraph maps. |
| L3 | final-translation | One translation to look at: evocative verse tracing to literal-gloss + essence. Frozen once loved. |
| L4 | song | The final translation set to music: prosody, rhythm, rhyme. Requires L3. |

Internal codes (T1, L0, …) **never change** — validators, gates, ledgers, packs,
lingua, treeka and the essay compiler all key on them. Public names are
additive: surfaces present `{code, public}` together and accept either on
input. Legend + resolver: `trika-x/formal-trika/data/layer-names.json`,
`tools/layer_names.py` (fail-closed; 6 tests green; 9/9 roundtrip proven).

## Scholar pipeline (draft → signoff)

`essay_compile` (verbatim quote bank + tiers) → essay-claim/1 typed claims →
`audit_draft` (same-paragraph verbatim binding) → PUSHBACK (cross-model destroy
pass; never edits the draft) → human sign → bridge → release → DOI.

- `essay_derive`: 6 essays, PARTIAL=6, BROKEN=0 (honest: no essay claims full
  derivability yet). Essay claims must bind a uniquely resolved ledger passage,
  matching complete-passage digest + source-edition field + verbatim span;
  duplicate locators and unsafe names refused.
- 14/14 `essay_check` tests green.

## Provenance model

Each layer file carries bytes + sha256 + status + where to re-fetch. A changed
byte invalidates downstream approval (recorded, never auto-healed). The decision
trail (who accepted which layer, when, on what grounds) is written at ingest by
the owning lane.

## Chunk identity

Locator (`tsa08-p03`) + `immutable_id` (`pt:pid:…`). Unknown/invented locators
are rejected, never prefix-resolved. `formal__bridge` resolves `chunk:<locator>`
to work/edition/etext rows; witness stays UNPINNED until manuscript eyes exist.
