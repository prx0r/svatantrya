# Ask four things — the Svatantrya workflow for a stranger
*Status: CANONICAL. User-facing one-pager for NORTHSTAR-2026-11-17. (2026-11-17.)*

You need: a ChatGPT (or Claude) account that can add an MCP connector, and the
URL `https://mcp.svatantrya.net/mcp`. No API key, no account, no install.

Ask these four things, in this order. Each answer arrives with its gaps named.

---

## 1. "What is the status of tantrasara-a08?"

One call (`openpatala__status`) returns the whole state:

```
work_id      tantrasara-a08
rights       NULL  (null rights = not publishable)
witnesses    0     (UNPINNED — editions are candidate strings)
editions 1 · etexts 1 · translations 1 · passages 4
formal       4/4 passages have a theorem reference (0 gaps)
traces       4 COMPLETE, but 4 chunk gates BLOCKED
layers       INDEXED
review       UNREVIEWED
```

Read it like this: **COMPLETE ≠ correct.** A trace is COMPLETE when every
applicable hop resolved; four gates are still BLOCKED (abstention and citation
grounding). The status object says both.

## 2. "What is a kañcuka?"

One call (`scholar__concept_get`) returns the concept card:

```
gloss_state  NO_CONCEPT_ENTRY  → no curated gloss exists; this is a gap
tier         T   (tradition-stated, argmap-pinned)
anchors      AnswerKey.lean :: key_five_kancukas
             Kancuka.lean   :: count_5
             Kancuka.lean   :: pairings_distinct
scope        MODEL_CHECKED inside the stated finite model only;
             doctrine claims are out of scope by contract
review       UNREVIEWED
```

Read it like this: the **counting** is machine-checked; the **meaning** is not.
The card refuses to give you a definition it does not have.

## 3. "Where does that appear?"

The same card carries occurrences (tokens, not readings):

```
6 occurrences across 4 works
  ipvv            chunk-v3-k-agama-prathamo-k8-11-close-v44
  paramarthasara  param-p02-v17
  paramarthasara  param-p03-v24
  parapravesika   par-p08-v08
  tantrasara-a08  tsa-a08-v55
  tantrasara-a08  tsa-a08-v56
```

Every locator comes from a tool. Verse-id → chunk-locator is a separate hop
(`formal__bridge`), and the card says so.

## 4. "Related points and essays."

One call (`treeka__chain`) returns argued nodes, cruxes, formal refs, essays,
and bridge state. Empty lists come back with a note:

```
essays: []  ← essays_note: "no essay bound to this passage — a gap, not a denial
              (corpus essayless: 331)"
formal: none ← formal_note: "no registry theorem references this passage
              (corpus no_formal_reference: 893)"
```

---

## What you can and cannot conclude

- **Can:** which texts exist, what layers they have, which structural claims are
  machine-checked, where a term occurs, what is missing and why.
- **Cannot:** that a translation is right, that a doctrine is true, or that a
  cleaned-up paraphrase is in the source. Nothing here is signed by a scholar;
  `UNREVIEWED` is the honest state of every claim today.

## For agents

The live server instructions carry the same four-turn order, so a cold session
follows it without being told. The acceptance test is
`tools/northstar_eval.py` (4/4 turns must pass cold).
