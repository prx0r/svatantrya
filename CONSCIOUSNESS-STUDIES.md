# CONSCIOUSNESS STUDIES — what "formalise it all fully" can and cannot mean
*Status: CANONICAL. Placement of Trika / aperture-inexternalism in consciousness
studies + the formalisation ladder. (2026-11-17.)*

*Companion to [THESIS.md](THESIS.md) §4a–4b. The comparison records live in
`svread/data/xmodel/comparisons.json`; the machine-checked core lives in
trika-x `frontier/Aperture.lean` and `frontier/Inexternalism.lean`.*

---

## 1. The answer in one line

**You can formalise the frame, not the identity.** The inventory, the operation,
and the exclusions are formalisable and are now formally checked. The phenomenal
identity `D_i ≡_inext O_i*` is a metaphysical identity across two modes of
access: Lean can encode it as a definition and prove its consequences; it cannot
prove the identity, and a formalisation that claimed to would be dishonest.

---

## 2. The formalisation ladder (what "fully" decomposes into)

| Layer | What it is | Formalisable? | State today |
|---|---|---|---|
| **A. Inventory** | the nine aperture operations | yes — finite list, distinct | **DONE** `Aperture.lean` (`aperture_nine`, `aperture_distinct`) |
| **B. Operation** | recognition as positioning-change only | yes — structure + 6 theorems | **DONE** `Inexternalism.lean`: `sigma_two`, `recognise_preserves_content`, `recognise_changes_positioning`, `recognise_involution`, `sample_closed`, `mode_switch_preserves_content` |
| **C. Exclusions** | what the theory forbids (e.g. experience is produced; experience floats free) | yes — as predicates + non-derivability | **PARTIAL**: encodable; not yet encoded |
| **D. Identity** | `D_i ≡_inext O_i*` | **as a definition, not a theorem** | defined conceptually; no theorem named "identity" (deliberate) |
| **E. Phenomenality / valence** | what it is like; felt quality | **no** — declared primitive, tier H | primitive, explicitly labelled |

**The twin that keeps layer B honest:** `BrokenInexternalism.lean` corrupts the
mode-switch so it alters content; `must_fail.py` requires the checker to refute
`mode_switch_preserves_content`. If the checker were vacuous, the twin would
pass. It does not.

**What layer D can honestly deliver:** a model in which the identity holds (so
the theory is consistent), plus the consequences the identity forces (so the
theory is not vacuous), plus the alternatives it rules out. That is the standard
formal treatment of an identity theory — not a proof of the identity.

---

## 3. Placement in consciousness studies (10 comparisons, 3 verdicts)

The engine enforces: **incompatible must name its obstruction; fit must name its
basis.** Six incompatibilities is not a failure — it is the actual finding.

| Theory | Verdict | The obstruction or basis |
|---|---|---|
| **HOT** (Rosenthal) | incompatible | quantifies over mental **states**; trika-x has no state-consciousness layer. Forced mapping contradicts on additivity (`recognition_adds_nothing` vs an added meta-state) |
| **IIT** (Tononi) | incompatible | **no causal graph, no Φ.** Φ is undefined, not merely uncomputed |
| **GWT** (Baars/Dehaene) | incompatible | no competition, no capacity limit, no broadcast. An ordering is not an architecture |
| **QRI valence** | incompatible | no qualia space, no metric, no valence function. A count of rasas is not a valence model |
| **Modal catuṣkoṭi** | incompatible | classical decidability vs paraconsistent "neither" |
| **Category-theoretic śūnyatā** | incompatible | **no morphisms** — Yoneda requires a category |
| **Active inference / free energy** | partial | boundary-formation maps to contraction; but one measurable boundary vs five named restrictions |
| **Allostasis** (Prueitt et al. 2025) | partial | apoha/exclusion maps; they say adaptation, we say removal of a covering |
| **PCT** (Mansell & Huddy) | partial | readiness gate maps; **sudden gains conflict with "no leaps"** |
| **Nāgārjuna-in-Lean** (Fujimoto 2026) | **fit** | methodological: both put the interpretive layer outside the kernel |
| **PCM** (Rudrauf et al.) | **partial, strengthened** | S = T ∘ R *is* our content-invariance; action group **proved Z/2** (generator + involution derived); one-carrier testbed built; continuity to PGL(4,R) named, not bridged |

**Field-level host (verified 2026-11-17):** *Formalizing consciousness: a
comparative mathematical analysis of leading theories*, Biological Cybernetics
(2026), doi `10.1007/s00422-026-01068-y` — a shared mathematical frame for AIF,
HOR and PCM. That is the right venue-type for the placement table, and it shows
the field already expects formal comparison rather than manifesto.

---

## 4. What would move an "incompatible" to "fit"

Each obstruction names the exact build that would change the verdict. This is
the roadmap, and it is deliberately expensive:

| Obstruction | What would have to be built | Status |
|---|---|---|
| no Φ (IIT) | a dynamics layer: a transition system over the finite states, then Φ |
| no broadcast (GWT) | competition + a capacity bound over the same states |
| no state ontology (HOT) | a level of mental states with a meta-relation; then test additivity |
| no qualia geometry (QRI) | a metric on the aesthetic modes; then a valence function |
| no morphisms (Yoneda) | a category whose arrows are the stipulated pairings, with a composition law | open |

**Do not build these to "win" the comparison.** Build one only if it buys a
prediction. The value of an incompatible verdict is that it stops the paper from
claiming a synthesis it does not have.

---

## 5. The paper this enables

Two papers, not one:

1. **Method paper (writable now).** "Formalising the frame, not the identity:
   what a proof assistant can and cannot do for consciousness theories." The
   aperture/inexternalism core is the worked example (core file + Z/2 action
   layer + cut result + testbed, 62 twins), with layers A–E named. The claim
   is methodological and defensible.
2. **Comparison paper (writable after review).** Trika in consciousness
   studies: 11 comparisons — 4 incompatible with named obstructions, 4 partial
   (one strengthened: PCM now has a proved Z/2 skeleton + testbed), 1 fit,
   2 not-comparable on scope grounds. The contribution is the *map of what does
   not connect*, which is more valuable than a fourth "everything is connected" essay.

**What neither paper may say:** that the phenomenal identity is proved, that
Φ has been computed, that a valence geometry exists, or that trika-x is a
theory of state consciousness.

---

## 6. Invariants

- Layer E is never formalised; it is declared.
- An identity claim is a definition plus consequences, never a theorem.
- A twin must fail at exactly one proposition, or the gate rejects it.
- BLOCKED ≠ PASS; incompatible ≠ refuted.
- Counts carry denominators: 226 theorems · 175 entries · 16/154 passages.
