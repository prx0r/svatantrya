# REPORT — Formalisation of the subtle body (puryaṣṭaka), compared with Vedānta (2026-11-19)

*Status: DELIVERED, machine-checked inside a finite model. NOT a doctrinal claim,
NOT peer reviewed, NOT published. Tiers below are load-bearing.*

---

## 1. Headline

The subtle body is now formalised **twice over**, because Abhinavagupta gives two
different eightfold formulas and says so himself:

- **Trika A (prāṇa-based)**: five vital breaths + buddhīndriya + karmendriya +
  antaḥkaraṇa = **8**; expanded into faculties, **18**.
- **Trika B (tanmātra-based)**: five tanmātras + manas + buddhi + ahaṃkāra = **8**.
- **Vedānta 17**: 5 prāṇas + 5 jñānendriyas + 5 karmendriyas + manas + buddhi.
- **Vedānta 19**: the same + ahaṃkāra + citta.

The machine checks the arithmetic **and** the non-identity of the partitions, so
"eight" cannot be equivocated.

---

## 2. Files

| File | Role |
|---|---|
| `trika-x/formal-trika/control/SubtleBody.lean` | comparative model (16 theorems) |
| `trika-x/formal-trika/control/BrokenSubtleBody.lean` | must-fail twin (6 prāṇas) |
| `trika-x/formal-trika/control/Puryastaka.lean` | the body itself (8 constituents, body = ahaṃtā) |
| `trika-x/formal-trika/control/BrokenPuryastaka.lean` | must-fail twin (7 constituents) |
| `trika-x/formal-trika/control/run.sh` | compiles both, then runs the twins |
| `trika-x/formal-trika/EVIDENCE.json` | 16 SubtleBody + 11 Puryastaka entries |
| `trika-x/formal-trika/bridge/passages.snapshot.json` | 239 pinned IDs (ĪPVV added) |
| `svread/topics/subtle-body.json` | answer-first public page + comparative matrix |
| `svread/topics/puryastaka.json` | the one-locus page |

---

## 3. What is proved (and what the proof means)

Lean 4.34.1, `-DwarningAsError=true`, exit 0.

| Theorem | Statement | Meaning |
|---|---|---|
| `trikaA_count` | total trikaA = 8 | formula A is eight |
| `trikaA_expanded_count` | total trikaAExpanded = 18 | expanded A is 18 |
| `trikaB_count` | total trikaB = 8 | formula B is eight |
| `vedanta17_count` | total vedanta17 = 17 | 17-part inventory |
| `vedanta19_count` | total vedanta19 = 19 | 19-part inventory |
| `same_cardinality` | total A = total B | both are "eight" |
| `not_same_partition` | kindsOf A ≠ kindsOf B | not the same partition |
| `partitions_disjoint` | A's kinds ∩ B's kinds = ∅ | no shared group kind |
| `eight_is_not_one_eight` | all three above at once | the comparative point |
| `expanded_differs` | 18 ≠ 8 | expansion breaks the coincidence |
| `vedanta19_adds_citta` | 19 = 18 + 1 | the single extra principle |
| `vedanta_17_19_gap` | 19 = 17 + 2 | ahaṃkāra + citta |
| `trikaA_vs_vedanta19` | 19 = 18 + 1 | cross-system gap |
| `prana_count_same` | 5 = 5 = 5 | count agrees everywhere |
| `prana_role_differs` | role(Trika) ≠ role(Vedānta) ≠ role(Vivekananda) | sense does not |
| `prana_same_count_not_same_definition` | same count ∧ trikaPrana ≠ vedantaPrana | rigid definition = (role, count) |

Plus `Puryastaka.lean`: `constituents_eight`, `partition_disjoint`,
`five_tanmatras`, `three_inner`, `kancukas_six`, `six_fewer_than_eight`,
`body_is_ahamta`, `city_is_body`, `burn_removes_body`, `burn_idempotent`,
`no_transmigration_without_body`.

**What is NOT proved:** that any inventory is metaphysically correct; that the
enumeration is the verse's own; that the kañcukas really contract the eight; or
any philological conclusion. The theorems are about the stipulated model.

---

## 4. Evidence (what each claim stands on)

### T — attested in our corpus (verbatim, chunk-bound)

| Claim | Chunk | Verse |
|---|---|---|
| Both formulas named; difference is `pakṣavaicitrya`, not `vastu-vaicitrya` | `ipvv:chunkV3-M-agama-dvitiyo-close-k12-20` | M00022:10000–10886 |
| Formula A: `prāṇādipañcakam indriyavargau … antaḥkaraṇa …` | same | same |
| Formula B: `tanmātrapañcakam antaḥkaraṇaṃ ceti kecana …` | same | same |
| Tanmātra list (TĀ 24.19) | `tantraloka-a24:tal-a24-p02` | 24.18–19 |
| Body-ness is ahaṃtā; burning removes it (TĀ 15.235–236) | `tantraloka-a15:tal-a15-p24` | 15.234–236 |
| No puryaṣṭaka → no heaven/hell (TĀ 24.21) | `tantraloka-a24:tal-a24-p03` | 24.21 |
| Six kañcukas contract the knower (TĀ 9.204–205) | `tantraloka-a09:tal-a09-p21` | 9.201–210 |

The ĪPVV passage is the keystone: Abhinavagupta **himself** distinguishes the two
formulas and denies the difference is in the thing.

### R — reconstructive / stipulated

- The eightfold enumeration as 5 tanmātras + manas + buddhi + ahaṃkāra: the
  verse list is compressed; the partition is supplied by the tradition.
- Prāṇa roles (vital breath / physiological function / cosmic force): a model of
  how the sources use the word, not an adjudication.

### X — external (cited, not in our Sanskrit corpus)

- Swami Medhananda, *Panentheism in Indian and Western Thought* (2023),
  "Abhinavagupta's Panentheism in Dialogue with Contemporary Neuroscience",
  ~p.13 — the prāṇa-based definition, citing Abhinavagupta 3:282 and Torella
  *ĪPK* p.132 v.1.6.4.
- Swami Medhananda, *Swami Vivekananda's Vedāntic Cosmopolitanism* (2022),
  pp.317–318 — liṅga/sūkṣmaśarīra (CW 2:456, 2:438).
- Maharaj (ed.), *The Bloomsbury Research Handbook of Vedānta* (2020), Śaṅkara
  chapter n.4 — subtle body: karmendriyas, jñānendriyas, prāṇas, mind.
- *Tattvabodha* / *Vedāntasāra* — the standard 17-part inventory.

---

## 5. Verification (reproduce)

```sh
# Lean model + mutants
cd /root/trika-x
PATH="$HOME/.elan/bin:$PATH" sh formal-trika/control/run.sh      # exit 0
python3 formal-trika/tools/evidence_check.py                     # 0 problems
python3 -m unittest discover -s formal-trika/tests -p 'test_*.py' # 138 OK

# public surface
cd /root/svread
python3 tools/emit_formal.py --check        # GREEN (202 theorems)
python3 tools/emit_topics.py --check        # GREEN
python3 -m unittest discover -s mcp -p 'test_*.py'  # 52 OK
node --test tests/*.cjs                      # 151 pass / 4 skipped

# read it
python3 tools/search_chunks.py "puryastaka"
#   -> ipvv, tantraloka-a24, tantrasara-a13, ... with the levels held per locus
```

Current measured state: **202 theorems**, **23/239 chunks referenced**,
**202 EVIDENCE entries over 31 works**, **910 traces** (231 COMPLETE).

---

## 6. Findings that came out of doing it

1. **The corpus already contained the comparative answer.** `chunkV3-M` states
   both formulas and reconciles them. The formalisation did not invent a
   comparison; it encoded one Abhinavagupta made.
2. **Two upstream defects were exposed and repaired** on the way:
   `spanda span-p04b` had no `immutable_id` (every pinned snapshot refused), and
   `source-map.json` ledger hashes were stale. Both are fixed in
   translation-work (PR #24) with a new `emit_source_map.py`.
3. **TĀ 9 and TĀ 15 gained full five-layer stacks mid-session** (upstream
   refresh), so the two strongest loci are now readable at L0/L2/ARGMAP, not
   just source. The topic pages were corrected rather than left stale.
4. **Counts in tests rot.** Three tests pinned coverage/passage counts; they were
   replaced with derived invariants so upstream growth cannot silently break CI.

---

## 7. Honest limits and next steps

- **Correction (2026-11-19): no secondary source is required for the Trika
  side.** An earlier draft of this report implied a Biernacki dependency.
  That was wrong: the primary witness is our own ĪPVV, already chunk-bound
  and quoted verbatim (`chunkV3-M`), and it *states both formulas and
  reconciles them*. Biernacki and Medhananda are corroboration (X), not
  evidence the argument stands on. Do not gate Trika claims on them.
- **The Trika corpus covers the doctrine broadly** (measured, `rg` over every
  `passages.jsonl`):

  | term | works | notes |
  |---|---|---|
  | `puryaṣṭaka` | **12** | ĪPVV 56 hits; Śivasūtravimarśinī 16; TĀ 8/9/15/24/29; Tantrasāra 8/13; Spanda; MV-vārttika; Gītārthasaṅgraha |
  | `prāṇa` | **44** | ĪPVV 160; Śivasūtravimarśinī 61; TĀ 6/7/15/29 |
  | `tanmātra` | 6 | ĪPVV 27; TĀ 8/9; Tantrasāra 8 |
  | `ahaṃkāra/ahaṃkṛti` | 7 | ĪPVV 22; TĀ 8/9/24 |
  | `kañcuka` | 10 | ĪPVV 11; Śivasūtravimarśinī 11; TĀ 6/8/15; Tantrasāra 6/8 |
  | `antaḥkaraṇa` | 4 | ĪPVV 37; Gītārthasaṅgraha 3; Śivasūtravimarśinī 2; TĀ 6 |

  So the formalisation is grounded in a corpus, not in a modern monograph.
- **Vedānta primaries are external.** `Tattvabodha`/`Vedāntasāra` are not in our
  located corpus, so Vedānta claims sit at X, not T. Ingesting them (a
  translation-work-style vector with chunk locators) is the single highest-value
  next step — it moves 4 theorems' evidence from X → T.
- **Mālinīnyāsa and pañcakośa are not formalised.** They are separate structures
  (ritual phonemic placement; five sheaths). `Nyasa.lean` is the template.
- **No publication yet.** The subtle-body material is ready for an expansion
  essay (it has chunk, theorems, tiers) but not drafted as one; and no essay has
  a DOI.

### Recommended next three jobs

1. `expansion-subtle-body` essay: compile from `ipvv:chunkV3-M` + `tal-a24-p02`
   with `SubtleBody.lean` theorems cited, claims bound to verse IDs, tension =
   `recognition-vs-individuation` (or a new `puryastaka-vs-kosha`).
2. Ingest `Tattvabodha` / `Vedāntasāra` (and optionally the Vivekananda CW
   passages) into a located corpus; re-tier the *Vedānta* evidence (the Trika
   side needs nothing added — see the corpus coverage table above).
3. Formalise `pañcakośa` and `Mālinī` as separate models, then a small
   `Comparison.lean` that states exactly where the four structures can and cannot
   map onto each other.
