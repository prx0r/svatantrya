# 00 — Thesis

## The goal (one line)

One question about a Trika text walks down to a witness and back up to a
signed, DOI'd essay — or a lesson, or a practice — with every link hash-pinned,
decision-tracked, gate-checked, and machine-verified where machines can verify.
**Commodity generation; scarce provenance.**

## Why this shape

AI generation is cheap and getting cheaper. What stays scarce is **provenance**:
knowing *which* text, *which* edition, *which* bytes a claim comes from, and
*which human* signed it. The estate is built to manufacture provenance at every
hop, so that anything the machine generates can be checked by an outsider with
nothing but `curl` and `sha256sum`.

## The chain (each hop: bytes + hash + status + where to re-fetch)

```
question
  → openpatala resolves work/edition (identity; UNRESOLVED = draft-only)
  → translation-work chunk + layers (evidence; each layer sha-pinned)
  → formal-trika Lean theorem + must-fail twin + run receipt (proof)
  → trace bundle (source bytes → layers → proofs → theorems; COMPLETE/PARTIAL)
  → essay claims → audit → PUSHBACK (cross-model destroy pass) → human sign
  → release → DOI → pack → video/lesson/practice
```

A hop that cannot name its input fails closed. Missing data is
UNKNOWN/UNPINNED, never filled by analogy or by a model guess.

## The two engines

- **The spine — formalisation as proof.** Lean's `decide` is the first estate
  component that *proves* instead of scoring: control checks (e.g. 8 mala-axis
  combos → exactly 7 well-formed experients) plus hand-written mutants that the
  checker is *required* to refuse. 53 control + 26 recognition checks green;
  206 theorems registered. Every rung ships with hash + grounds + gate + signer
  role, or it does not ship.
- **The geometry — the phonemic body.** The Mālinī order (50 phonemes × loci ×
  Śaktis × 5 maps) is the frontier the spine grows into: the first
  comparative-formal rung plus visual truth. Frontier consumes the whole
  machine; it is the first customer, not the foundation.

## Tiers (on every load-bearing claim)

| Tier | Meaning |
|---|---|
| T | root text |
| R | reconstruction (AM0, inexternalism, CSID — never smuggled as T) |
| E | empirical |
| C | correspondence |
| H | hypothesis |
| X | rejected |

A reconstruction may never promote itself. R never becomes T without a human.

## Rules (inherited by every repo)

1. Prereg before code; corrections are new dated files, history never edited.
2. Machine proposes, human disposes. No auto-sign, no auto-publish.
3. Tiers on everything. R never promotes itself.
4. Fail-closed. Timeouts/blocks/empties are ERRORS, never passes.
5. No rung ships without hash + decision/grounds + gate + signer-role.
6. Only `decide` proves, inside its stated finite scope. Heuristic PASS ≠ proof.
7. Lanes respected: read other lanes' repos, never write their files.
8. One identity system: openpatala is the root. No second DB, ledger, or ID scheme.
9. Private stays private: diary material ships only with explicit, scoped, revocable consent.

## What "done" means (per track)

- **Identity:** queryable populated DB; edition pins honest; restore recipe exists.
- **Chunks/layers:** source records complete; nodes indexed; treeka + gaps live.
- **Formal:** coverage climbing per rung, prereg-first; blind pilots; twin review.
- **Essays:** PUSHBACK live; chain integration tested; Zenodo dry-run ready.
- **Teaching/practice:** study units rendered; eligibility + day gates; body-map checked.
- **Bench:** calibration + thresholds on CPU; tau when quota allows.
- **Geometry:** schema + readiness + comparison scaffold + reconstruction inventory.
- **Corpus/biblio:** atlas seeds flowing into the box DB; bibliography by reference.
