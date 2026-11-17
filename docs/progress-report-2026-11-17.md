# PROGRESS REPORT — 2026-11-17
*Status: HISTORICAL. Session record: what was built, what was measured, what
broke, what is owed. (2026-11-17.)*

*Method: gates re-run on the box (Lean 4.34.1 control + recognition, evidence
check, table, axiom audit, catalog, full suite), live MCP probes against
`mcp.svatantrya.net`, `doc_check.py --all-warns`, `pytest tools/test_doc_check.py`,
and unit suites in three repos. Live numbers are from this session unless a date
is given.*

---

## 1. What this session was

Two owner northstars were received and saved verbatim, and the project's own
conception of itself moved twice in one day. This report records the build that
followed, and the four places where the machinery caught the agent making things
up.

**Verbatim sources written today (never to be edited):**

- `NORTHSTAR-2026-11-17.md` — one system: work status → concept card →
  occurrences → essays.
- `NORTHSTAR-2-2026-11-17.md` — Trika as intellectual source, not public
  identity; general theory of psychological transformation; F research tracks.

**Programme documents written today:**

- `THESIS.md` — philosophy is for humans; three propositions kept separate; F1–F12.
- `CONSCIOUSNESS-STUDIES.md` — formalisation ladder A–E; 10 comparators.
- `MASTERPLAN4.md` — plan of record for this phase.
- `docs/papers/P1-formalising-the-frame-2026-11-17.md` — method paper draft.
- `docs/papers/P2-trika-in-consciousness-studies-2026-11-17.md` — comparison
  paper draft.
- `docs/northstar-user-guide.md` — stranger-facing four-turn guide.

---

## 2. Delivered: the four-turn workflow (NORTHSTAR 1)

Baseline at session start: **T1 partial, T2 fail, T3 fail, T4 partial.**

Now: **4/4 OPERATIONAL**, measured by `tools/northstar_eval.py`, p95 1.55 s
(T1 1.6 s · T2 0.25 s · T3 shares T2 · T4 1.5 s).

| Turn | What was added | Repo |
|---|---|---|
| T1 status | `openpatala__status` — one call: identity, rights, witnesses, counts, per-work formal coverage, trace verdicts **with blocked gates**, layer state, review state, provenance | openpatala #5 |
| T2 concept | `scholar__concept_get` + `emit_concepts.py` — 415 concepts, 345 with occurrences; gloss-or-stated-absence | svread #70 |
| T3 occurrences | term→locus index from a single diacritic-folded pass over L0; kañcuka = 6 across 4 works | svread #70 |
| T4 related | `treeka__chain` annotates empty essays and unformalised rows; no silent `[]` | svread #70 |
| gate fix | `formal__evidence` accepts bare theorem names; `formal__gaps` counts passages only (16/154, 138 gaps, arithmetic consistent) | trika-x #33 |
| instructions | live bundle instructions carry the four-turn order | svread #70 |

**Not done:** the status object still does not name the base *edition* (title or
URI). That is the next real hole, not a cosmetic one.

---

## 3. Delivered: the comparative layer (NORTHSTAR 2 / THESIS)

- `tools/xmodel.py` — **11 cross-model tensions**; every Trika anchor must
  resolve in `EVIDENCE.json`; unformalised interlocutors require an
  `asymmetry_note`; every tension carries a `settling_condition`; status flips
  are human-only.
- `tools/compare.py` — **10 comparisons against published formalisations**;
  verdicts `fit | partial | incompatible`; incompatible must name its obstruction,
  fit its basis; essays are generated **structurally** from the record.
- `xmodel:` joins the shared-language ID grammar (`lingua.resolve`).
- Essays: **10/10 pass the essay gate** (`READY_FOR_HUMAN_REVIEW`, not approval).

Verdict distribution: **6 incompatible, 3 partial, 1 fit.**

---

## 4. Delivered: aperture / inexternalism core (layer B)

`frontier/Inexternalism.lean` (tier H, owner framework): two positionings, a
field ⟨knower, world, relation, positioning⟩, recognition as positioning-flip.
Six theorems, including `recognise_preserves_content`, `recognise_involution`,
and `mode_switch_preserves_content`. No theorem is named *identity* — the
metaphysical identity is encoded as a definition and deliberately not proved.

Twin `BrokenInexternalism.lean` corrupts the mode switch; `must_fail.py` requires
the checker to refute `mode_switch_preserves_content`. Control gate: **PASS**.

---

## 5. Number cross-check

| Quantity | Before session | After | Command |
|---|---|---|---|
| EVIDENCE | 206 thm · 161 entries | **214 · 159** | `formal-trika/tools/evidence_check.py` |
| MCP catalog | 115 tools | **118** | `tools/mcp_catalog.py --check` |
| Full suite | 138 (1 skip) | **138 (1 skip)** | `unittest discover -s formal-trika/tests` |
| Twins | 57 | **58** | count `must_fail` pairs |
| Coverage | 16/154 | **16/154** (live was self-contradicting 17+138=155) | `formal__gaps` live |
| Concepts | none | **415** (345 with occurrences) | `emit_concepts.py --check` |
| Xmodel tensions | none | **11** | `tools/xmodel.py check` |
| Comparisons | none | **10** | `tools/compare.py check` |
| Essays through gate | 6 | **10** | `essay_check.py --all` |
| Four-turn workflow | 0/4 | **4/4** | `tools/northstar_eval.py` |

Drift corrected in canonical docs: mutants 79 → **57**; suite 107 → **132**
(PAPER, 30, 60, 80); theorem/entry counts updated to 214/159.

---

## 6. Findings (things that were wrong, all recorded)

**F1 — a catalog drift caused by adding tools.** Adding `openpatala__status` and
two scholar concept tools moved the live catalog from 115 to 118, and
`test_catalog_matches_live_when_full` failed. This is the gate working: tool
additions require `tools/mcp_catalog.py --write`. Done, then green.

**F2 — the type logic caught two hallucinated anchors.** `xmodel.py` rejected
`Recognition.lean :: recognition_unique`; the theorem is in `Conjuncts.lean`.
`compare.py` rejected the same mistake in a second record. Two independent
checks caught the same class of error. Without the gates, both would have
shipped.

**F3 — six comparisons initially failed their own rules.** They were comparing a
formalised model to an unformalised one without saying so. Adding
`asymmetry_note` to each is not cosmetic: it is the difference between a
comparison and a con.

**F4 — the essay gate hard-coded `tension:`.** A cross-model tension
(`xmodel:`) was rejected even though the shared-language resolver resolves it.
The gate now accepts any atom the resolver knows. The prefix is not the type;
resolution is.

**F5 — Cloudflare 403s the default Python user-agent.** The acceptance harness
worked under `curl` and failed under `urllib`. A named client UA is required; the
harness now sends one, with the reason in a comment.

**F6 — `openpatala__resolve` takes `q`, not `query`.** A schema detail a model
handles from the tool schema, but a human script must know. Recorded in the
northstar.

---

## 7. What is owed (owner-held, cannot be closed by an agent)

1. **Verdict review.** Six `incompatible` verdicts and three `partial` verdicts
   need a named human acceptance before any paper cites them.
2. **Witnesses: 0.** Every T-tier claim is `UNPINNED` at manuscript level. No
   amount of formalisation changes this.
3. **Token rotation** (shared MCP bearer, pasted GitHub token).
4. **DOI**: no Zenodo token, so no first release.
5. **Search Console / indexing** and OAuth remain owner switches.

---

## 8. Reproduction commands

```sh
# trika-x
python3 formal-trika/tools/evidence_check.py
python3 formal-trika/tools/table.py --check
python3 formal-trika/tools/axiom_audit.py --check
python3 tools/mcp_catalog.py --check
python3 -m unittest discover -s formal-trika/tests
PATH=/root/.elan/bin:$PATH sh formal-trika/control/run.sh
PATH=/root/.elan/bin:$PATH sh formal-trika/recognition/run.sh
python3 formal-trika/tools/essay_check.py --all

# svread
python3 tools/xmodel.py check
python3 tools/compare.py check
python3 tools/emit_concepts.py --check

# svatantrya
python3 tools/doc_check.py --all-warns
python3 -m pytest tools/test_doc_check.py -q
python3 tools/northstar_eval.py
```

*Machine proposes, human disposes. BLOCKED ≠ PASS. A verdict is not a refutation.*
