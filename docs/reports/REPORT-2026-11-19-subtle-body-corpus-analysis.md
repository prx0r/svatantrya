# REPORT — Corpus analysis: the subtle body across the Trika works (2026-11-19)

*Status: ANALYSIS + DELTA. Scope is every work with a passage ledger in
`/root/translation-work`. Counts are surface matches; roles are keyword tags
over ±300-char windows; every quoted locus resolves in `passages.jsonl`.
The formalisation delta is in `trika-x/formal-trika/control/SubtleBodyCorpus.lean`.*

---

## 1. Scope (measured)

```sh
# 96 works, 1,035 chunks, ~7,050 verses
python3 - <<'PY'  # see docs/reports/data/ for the emitted artefacts
PY
```

- **96 works** with `passages.jsonl`; **1,035 chunks**; **≈7,050 verses**.
- Trika core: Tantrāloka 1–37 (≈5,700 v.), Tantrasāra 1–22 (≈1,000 v.),
  ĪPVV 1–3 (49 chunks), Śivasūtravimarśinī, Spanda, VBT, PTv, MV-vārttika,
  Gītārthasaṅgraha, plus the stotra corpus. Kularṇava is present as āgama
  context without layers.
- **84 `puryaṣṭaka` occurrences across 12 works**; `prāṇa` in **44 works**.

Artefacts (committed):

- `docs/reports/data/puryastaka-hits-2026-11-19.json` — every occurrence with
  work, locator, verse label, immutable id, ±300-char window, keyword roles.
- `docs/reports/data/puryastaka-corpus-2026-11-19.json` — per-work term matrix.

---

## 2. Term matrix (surface counts)

| work | puryaṣṭaka | prāṇa | tanmātra | indriya | antaḥkaraṇa | kañcuka | ahaṃtā |
|---|---:|---:|---:|---:|---:|---:|---:|
| ipvv | **56** | **160** | 27 | 111 | 37 | 11 | 114 |
| sivasutravimarsini | **16** | 61 | 6 | 5 | 2 | 11 | 8 |
| tantraloka-a09 | 1 | 1 | 8 | 1 | 0 | 3 | 1 |
| tantraloka-a15 | 2 | 13 | 0 | 0 | 0 | 1 | 1 |
| tantraloka-a24 | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| tantraloka-a29 | 1 | 8 | 0 | 0 | 0 | 0 | 0 |
| tantrasara-a08 | 1 | 1 | 4 | 1 | 0 | 2 | 1 |
| tantrasara-a13 | 1 | 3 | 0 | 0 | 0 | 0 | 1 |
| spanda | 1 | 0 | 1 | 0 | 0 | 0 | 0 |
| gitarthasangraha | 1 | 7 | 0 | 19 | 3 | 1 | 0 |
| malinivijayavarttika | 1 | 11 | 3 | 6 | 0 | 4 | 0 |
| tantraloka-a08 | 1 | 3 | 7 | 0 | 0 | 1 | 0 |

The doctrine is not a single-chapter curiosity: it runs through the
Pratyabhijñā commentarial line (ĪPVV, ŚSV), the Tantrāloka/Tantrasāra, the
Spanda, Abhinavagupta's Gītā commentary, and his MV commentary.

---

## 3. Four results of the pass

### 3.1 There are THREE formulas, not two

| | formula | source | count |
|---|---|---|---:|
| **A** | 5 prāṇas + buddhīndriya + karmendriya + antaḥkaraṇa | ĪPVV `chunkV3-M`; MV-vārttika `mv-k02`; Gītā `gita-a15`; ŚSV (jīva clause) | 8 (expanded 18) |
| **B** | 5 tanmātras + manas + buddhi + ahaṃkāra | TĀ 24.19; Spanda `span-p06`; ĪPVV ("kecana … āhuḥ") | 8 |
| **C** | 5 tanmātras + the three **guṇas** | Śivasūtravimarśinī `ssv-u3` (Kṣemarāja) | 8 |

ĪPVV already says the A/B difference is `pakṣavaicitrya`, not
`vastu-vaicitrya`. C shows a third vocabulary: rajas→manas, tamas→ahaṃkāra,
sattva→buddhi. Same count, different partition *and* different vocabulary.

### 3.2 There is a three-level body schema

TĀ 29.261–270 (`tal-a29-p27`):

> `piṇḍaḥ paraḥ kalātmā sūkṣmaḥ puryaṣṭako bahiḥ sthūlaḥ`

the piṇḍa (supreme/kalā-self), the **subtle puryaṣṭaka**, and the outer gross
body. ŚSV calls the puryaṣṭaka the `sūkṣmaśarīra` and the cause (`kāraṇa`) of
the gross body. This is the Trika analogue of the three-body (causal/subtle/
gross) schema — in Trika terms, not imported.

### 3.3 Its functions are attested, not inferred

- **Transmigration**: Gītā `gita-a15` (on BG 15.8), `puryaṣṭakena saha`;
  TĀ 24.21, without the puryaṣṭaka no heaven/hell; ŚSV, the subtle body
  migrates while the gross is dropped.
- **Purification**: TĀ 24.20, `puryaṣṭakaviśodhanī` dīkṣā; TĀ 8.23x,
  `śodhayed buddhiṃ sārdhaṃ puryaṣṭakendriyaiḥ`.
- **Liberation**: TĀ 15.235–236, body-ness = ahaṃtā and its destruction is
  liberation; Tantrasāra 13.24, burn `dehatā` by abandoning `ahambhāva`;
  ŚSV, `puryaṣṭakapramātṛtābhimānavigalana`.
- **Prāṇa pervades it**: MV-vārttika `mv-k02`, `prāṇaḥ puryaṣṭakaṃ dehaṃ
  vyāpya viśvaṃ prakarṣati`.
- **The jīva is governed by it**: ŚSV, `prāṇapuryaṣṭakaniyantrito jīvaḥ`.

### 3.4 Two loci are still unpinned

`malinivijayavarttika:mv-k02` and `gitarthasangraha:gita-a15` are quoted as
**r_sources** (not chunk-bound) because those works are not yet in the pinned
snapshot. Pinning them is mechanical (they have ledgers); it was left out to
avoid widening the snapshot mid-change. Until then their tier is **R-source**,
not T-chunk.

---

## 4. Formalisation delta (`SubtleBodyCorpus.lean`)

Machine-checked additions (Lean 4.34.1, exit 0; must-fail twin on `C_count`):

| theorem | content |
|---|---|
| `A_count`, `B_count`, `C_count` | each formula totals 8 |
| `three_formulas_eight` | all three at once |
| `B_C_same_count`, `B_C_different_vocabulary` | C is not B re-lettered |
| `A_disjoint_B`, `A_disjoint_C` | A shares no group kind with either |
| `guna_inner_same_count`, `gunas_distinct`, `inner_distinct` | guṇa/inner-organ correspondence is cardinal, not identity |
| `guna_inner_not_identical` | the model refuses to identify the kinds |
| `three_levels`, `levels_distinct` | piṇḍa / subtle / gross |
| `migration_at_subtle`, `gross_not_carried`, `pinda_not_carried`, `exactly_one_carried` | one carrier |
| `city_units`, `prana_pervades_city` | the city is eight; prāṇa is within |
| `liberation_drops_bodyness`, `liberation_keeps_units` | ahaṃtā goes, constituents stay |

Registry: EVIDENCE **224 entries over 33 works**; snapshot **272 IDs**;
coverage **26/272 chunks referenced** by formal entries. All 138 trika-x tests
pass; `evidence_check` 0 problems.

---

## 5. Reproduction

```sh
# analysis artefacts
python3 - <<'PY'   # script reproduced in the session log
PY
# see docs/reports/data/puryastaka-*.json

# formalisation
cd /root/trika-x
PATH="$HOME/.elan/bin:$PATH" sh formal-trika/control/run.sh
python3 formal-trika/tools/evidence_check.py

# public surface
cd /root/svread
python3 tools/emit_formal.py --check
python3 tools/emit_topics.py --check
python3 tools/search_chunks.py "puryaṣṭaka"
```

---

## 6. What this changes, and what it does not

**Changes:** "the Trika subtle body" can no longer be quoted as a single
eight-item list. Three attested formulas exist, plus a three-level schema and a
functional profile (migration, purification, liberation). The formal model now
holds all of that, with the partitions kept distinct.

**Does not change:** the tiers. A/B/C counts and level names are T where
chunk-bound; the guṇa→inner-organ mapping is R (the text makes it, the model
does not identify the kinds); the MV/Gītā loci are R-source until pinned. No
doctrine is proved; no publication exists.

---

## 7. Next (small, ordered)

1. Pin `malinivijayavarttika` and `gitarthasangraha` (add to snapshot/map);
   upgrade their two loci from R-source to T-chunk.
2. Compile `expansion-subtle-body` from `ipvv:chunkV3-M` + `tal-a24-p02` +
   `ssv-u3`, citing the v2 theorems, claims bound to verse IDs.
3. Formalise `pañcakośa` (five sheaths) and `Mālinīnyāsa` separately; then a
   small `Comparison.lean` for the four structures.
