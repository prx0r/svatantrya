# Trika in Consciousness Studies
## A map of what does not connect, and why that is the result

*Status: DRAFT — machine-compiled under owner direction, not peer reviewed, no
DOI, no human sign-off, and every verdict awaits a named human reviewer.
2026-11-17.*

---

## Abstract

Comparative work between a metaphysical tradition and consciousness science
usually proceeds by theme matching: both discuss the self, therefore they can be
compared. We argue this produces equivocation, and propose instead a
**signature check**: state the formal object each theory requires, state what the
other theory actually provides, and record a verdict of `fit`, `partial`, or
`incompatible` — where *incompatible requires naming the precise obstruction*.
We apply the method to Trika Śaivism as encoded in a machine-checked corpus
(225 theorems, 159 registry entries, 57 negative-control twins) against ten
interlocutors. Result: **one fit, four partial mappings, four incompatibilities with named
obstructions, and two cases that are not comparable because they answer a
different explanatory question.** We argue the six are the
contribution: they identify exactly where a synthesis would be equivocation, and
each names the build that would change its verdict. We also report one
methodological disparity with a sibling formalisation — an axiomatic Advaita
encoding lists "liberation as recognition" among what it cannot capture, while a
finite-table Trika encoding proves it — and argue that this is a claim about
method, not doctrine.

**Keywords:** Trika Śaivism; Pratyabhijñā; formal ontology; consciousness
studies; comparative philosophy; Lean 4.

---

## 1. The failure mode

Theme matching has a predictable failure: two theories both use the word "self",
a comparison is written, and no claim in the comparison can be false because no
shared formal object was ever specified. The output reads as synthesis and is
actually paraphrase.

The alternative is not scepticism. It is **specification**. For each pair, ask:

1. What **object** does their theory quantify over (states? processes?
   structures? measures?)?
2. What **signature** does their central term require (a transition system? a
   meta-relation? a metric?)?
3. Does the other theory *have* that object and signature, or only a word that
   sounds like it?

A verdict follows mechanically, and the interesting verdicts are the negative
ones.

---

## 2. Method, and the level discipline

Following the comparative method of Yan et al. (2026, *Biological Cybernetics*),
every comparison declares the **scope** of the question each side answers. An
`incompatible` verdict is only legal when both sides answer the *same* question;
a different question yields `not-comparable`, which must name the difference.
This matters: two of our original six "incompatibilities" were scope mismatches,
not contradictions, and were reclassified (HOT, QRI). Every record also names the
**formal tools** the comparison requires and the **tractability** of both sides —
ours is `O(n)` enumeration over finite tables, which is a containment advantage,
not a coverage one.

Every comparison is a record with: the interlocutor's artefact and citation; the
trika-x anchors (each of which must resolve in the registry or the record is
invalid); at least one shared axis and one disparity, each with a stated
consequence; a verdict; and — mandatory for `incompatible` — the obstruction, and
for `fit` — the basis. Ten records are enforced by a checker; nothing flips a
verdict on its own.

Two rules keep this honest:

- **Incompatible ≠ refuted.** A verdict says the translation fails, not that the
  interlocutor is wrong.
- **Partial must say which axis maps and which does not.** "Mostly fits" is not a
  verdict.

---

## 3. The six incompatibilities

| Theory | Signature it requires | What trika-x provides | Obstruction |
|---|---|---|---|
| **HOT** (Rosenthal) | a predicate on mental *states*, plus a meta-representation relation | self-positioning over a finite field; no state-consciousness layer | **different objects of quantification.** Forced mapping contradicts on additivity: HOT needs an *added* higher-order state; trika-x proves `recognition_adds_nothing` |
| **IIT** (Tononi) | a transition system and an irreducibility measure Φ | inductive types, an enumerating check, no dynamics | **Φ is undefined, not uncomputed.** No causal graph exists to measure |
| **GWT** (Baars/Dehaene) | competition for a capacity-limited broadcast | an exhibited partial order | **no competition, no capacity limit, no broadcast.** An ordering is not an architecture |
| **QRI valence** | a qualia space with symmetries and a valence function | a finite inventory of aesthetic modes (nine rasas) | **no space, no metric, no valence function.** A count is not a geometry |
| **Modal catuṣkoṭi** (Chapman 2026) | non-classical valuation to carry "neither" | classical decidable propositions (`by decide`) | **decidability vs paraconsistency.** The fourth lemma is not a decidable classical proposition |
| **Category-theoretic śūnyatā** (Roy & Posina 2024) | a category: objects plus composable arrows | types plus a restricting function | **no morphisms.** Yoneda cannot even be stated |

Each obstruction is a *build order*, not an insult: §6 states what would have to
exist for the verdict to change.

---

## 4. The three partials and the one fit

**Active inference / free energy** (partial). Their self is a Markov blanket, a
statistical boundary between internal and external states; Trika's is five named
coverings, each restricting one capacity. The mapping holds on
boundary-formation and breaks on cardinality: either the five collapse into one
precision parameter, or the blanket account is under-specified for persons.

**Allostasis** (partial). Prueitt, Sezer and Sacchet (2025) already bridge
Pratyabhijñā and allostasis for pain, using exclusion (*apoha*) to constitute the
boundary — an unusually close methodological precedent. The disparity is real:
they model pain as a command to *adapt* a boundary (homeostatic or heterostatic);
the Trika covering-chain models *removal* by ascent.

**Perceptual Control Theory** (partial). Chronic unresolved goal conflict maps
onto contraction; awareness enabling reorganisation maps onto recognition. But
PCT reports **sudden, durable gains**, and trika-x proves `abandon_strict` — every
resort ascends exactly one rung, no leaps. This is a genuine falsifiable conflict,
not a verbal one.

**Nāgārjuna in Lean 4** (fit). Not a doctrinal fit but a methodological one: that
project declares a verification boundary — "Lean verifies the combinatorics; the
mapping to Madhyamaka concepts is a separate interpretive layer, NOT verified by
Lean" — which is the same discipline trika-x enforces through tiers and a
`MODEL_CHECKED` scope note. Two independent Lean encodings of Indian philosophy
placing the interpretive layer outside the kernel is a stronger claim than either
alone.

---

## 5. The Advaita disparity (the sharpest single result)

An axiomatic formalisation of Advaita Vedānta in Lean 4 (129 primitive axioms,
ten modules, master theorems for `Tat Tvam Asi` and the three-state analysis)
includes, under *what the formalization cannot capture*:

> "Liberation as recognition. Mokṣa is not the production of a new state but the
> recognition of what was always the case."

A finite-table formalisation of Trika proves exactly that claim:
`recognition_adds_nothing` and `recognition_preserves_content`, by `decide`, with
a twin that must fail.

The disparity is **methodological, not doctrinal**. An axiomatic method that
begins from an assumed absolute cannot easily express an operation that adds
nothing, because the apparatus is built to derive properties of the absolute. A
finite enumeration of the operation's *content and positioning* can express it
directly. Neither method is refuted. But the claim "recognition is
unformalizable" is shown to be false as stated, and the reason is instructive:
what resisted formalisation was not the doctrine but the axiomatic frame.

---

## 6. What would change each verdict

| Obstruction | The build that would remove it |
|---|---|
| no causal graph (IIT) | a transition system over the finite states; then Φ can at least be defined |
| no broadcast (GWT) | competition and a capacity bound over the same states |
| no state ontology (HOT) | a level of mental states with a meta-relation; then test additivity |
| no qualia geometry (QRI) | a metric on the aesthetic modes; then a valence function |
| no morphisms (Yoneda) | a category whose arrows are the stipulated pairings, with a composition law |

The recommendation is **not** to build all of these. Build one only if it buys a
prediction. A verdict of `incompatible` with a named obstruction is more valuable
than a synthesis that cannot be falsified.

---

## 7. What this says about Trika

Three claims follow from the map, each narrower than the usual synthesis.

1. **The affirmative ontology buys classical tractability and costs the fourth
   lemma.** Trika's manifestation-affirming structure is decidable; that is why
   `decide` works and why the catuṣkoṭi's "neither" cannot be represented. This
   is a design commitment, not an oversight.
2. **Contraction is five typed restrictions, not one boundary.** The
   Markov-blanket comparison is the most seductive in the set precisely because
   it is nearly right; the cardinality gap is where the work is.
3. **Recognition is content-preserving.** This is the claim with the widest reach
   — it conflicts with HOT's additivity, with learning-model accounts of change
   as evidence accumulation, and with any therapy model that measures insight by
   information delivered.

---

## 8. Limitations

- Witnesses: **zero**. Editions are candidate strings; every T-tier claim in the
  corpus is UNPINNED at the manuscript level. This paper's textual claims inherit
  that limitation.
- No soundness or faithfulness theorem for the trika-x encoding. The defence is
  non-vacuity (62 twins), which is weaker and is not presented as soundness.
  Position stated in trika-x `formal-trika/SOUNDNESS.md`.
- Interlocutor positions are recorded as published and were **not** re-verified in
  the same session as the proofs; four theory citations are standard references
  not re-checked at all.
- Verdicts are machine-recorded but **human-unreviewed**. `UNREVIEWED` is a
  state, not a verdict.
- Coverage: 16 of 154 passages carry a theorem reference. The map describes what
  exists, not the tradition.

---

## 9. Conclusion

The useful comparative result is not that Trika and consciousness science agree.
It is that a disciplined comparison can say exactly where they cannot be
translated, name the signature each theory requires, and specify what would have
to be built to make the translation possible. Six such obstructions, one
methodological fit, and one sharp disparity between two formalisations of Indian
philosophy are more defensible than any amount of thematic synthesis — and they
are checkable, which is the only thing that matters if the tradition is to enter
the conversation on terms it can survive.

---

## References

**Verified in-session (2026-11-17) — primary or multi-source fetches:** Prueitt, Sezer & Sacchet (2025) [PMC12687940, fetched],
*Neuroscience of Consciousness* niaf049; Berwian et al. (2025), *Communications
Psychology* s44271-025-00251-4; Smith, Moutoussis & Bilek (2021) PMC8115057;
Mansell & Huddy (2020) *Frontiers in Psychiatry* fpsyt.2020.00624; Schiepek, Aas &
Viol (2016) PubMed 27262423; arXiv:2511.05580 [abs page fetched; PDF content via verified excerpts]; arXiv:2509.02144 [abs page fetched with full abstract];
arXiv:2605.12548; Chapman (2026) *Comparative Philosophy* 17(2);
doi:10.1163/9789004691568_026; Tavva & Singh (2015) CEUR-WS Vol-1517; Fujimoto
(2026) doi:10.5281/zenodo.20838891; Scherf, github.com/matthew-scherf/Advaita;
Yan et al. (2026) *Biological Cybernetics* doi:10.1007/s00422-026-01068-y **[abstract + metadata only; full text not read]**;
Kirchhoff et al. (2018) PMC5805980.

**Standard references, not re-fetched this session** (textbook-level claims; re-fetch before submission): Rosenthal (HOT); Tononi and
colleagues (IIT); Baars / Dehaene and colleagues (GWT); Johnson and colleagues
(QRI symmetry theory).
