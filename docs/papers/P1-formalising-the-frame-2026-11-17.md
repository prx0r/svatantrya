# Formalising the Frame, Not the Identity
## A layered method for machine-checking consciousness theories, worked on aperture inexternalism

*Status: DRAFT — machine-compiled under owner direction, not peer reviewed, no
DOI, no human sign-off. Cite the repository commit, not this file, if you need a
fixed target. 2026-11-17.*

---

## Abstract

Theories of consciousness that identify experience with a physical or
functional process are rarely formalised, and when they are, the formalisation
usually proves something adjacent to the central claim and presents it as the
central claim. We propose a five-layer decomposition that makes the boundary
explicit: **inventory, operation, exclusion, identity, phenomenality**. Layers
A–C are formalisable; D is encodable as a definition with provable consequences
but cannot be proved; E is a declared primitive. We work the method on *aperture
inexternalism*, an identity theory in which one concrete process is described
extrinsically as an embodied aperture and intrinsically as a valenced phenomenal
field. In Lean 4 we encode the two positionings, the recognition operation, and
the mode-of-access switch; twelve theorems are machine-checked in the core file
(a positioning inventory, content preservation, involution, mode-switch
invariance, two exclusion constraints), plus a Z/2 action layer proving the flip
is the generator of exactly the symmetry group this structure admits, plus a
cut result with no cross-block flow. Each has a hand-written twin that a named
proposition must refute. We prove content preservation,
involution, and non-fixed-point; we do **not** prove the identity, and no theorem
is named for it. We argue that this is the correct formal treatment of an
identity theory, and that the discipline transfers to any theory with a
metaphysical identity at its core.

**Keywords:** formal philosophy; Lean 4; identity theory; consciousness studies;
negative controls; verification boundary.

---

## 1. The problem

Three things go wrong when a consciousness theory is formalised.

1. **Phenomenal smuggling.** A predicate named `conscious` or `experience` is
   introduced and then used as if its interpretation were secured by the
   formalism. It is not: the formalism secures only that the symbols are
   consistent with each other.
2. **Selector smuggling.** A model of *what is experienced* is silently treated
   as a model of *which process is the subject*. The second is an individuation
   claim and is usually not formalised at all.
3. **Identity inflation.** An identity claim is stated as a theorem because the
   encoding makes both sides the same type. `theorem experience_is_process :
   Experience = Process := rfl` proves only that the author wrote the same
   definition twice.

This paper's contribution is not a new theory. It is a **decomposition that
makes these three failures detectable**, plus a worked encoding showing what the
honest maximum is.

---

## 2. The five layers

| Layer | Content | Formalisable | Criterion |
|---|---|---|---|
| **A. Inventory** | the named functional roles the theory asserts | **yes** | finite, distinct, and no semantic claim beyond names |
| **B. Operation** | what the theory says changes (and what does not) | **yes** | a function on a stated carrier, with preservation/variance proved |
| **C. Exclusion** | what the theory forbids | **yes, as predicates** | each exclusion is a decidable or provable non-derivability claim |
| **D. Identity** | the metaphysical identity between two descriptions | **definition only** | consistency + consequences + ruled-out alternatives; never a theorem |
| **E. Phenomenality** | what it is like; valence | **no** | declared primitive, tier-labelled, never modelled |

Placing these at Marr's levels makes the boundary sharper: layers A–C are
**computational-level** descriptions (what is computed, not how), layer D is a
metaphysical identity that no level fully captures, and layer E is not an
implementation claim at all. Following Yan et al. (2026), a comparison that
ignores level will manufacture contradictions out of scope differences.

Two rules follow.

**Rule 1.** A formalisation must state which layer each theorem belongs to. A
layer-B theorem is not evidence for a layer-D claim.

**Rule 2.** Layer E may appear in definitions but never in a proof's conclusion.
Any theorem whose statement contains a phenomenal predicate is a layer-E claim in
disguise and must be labelled as such.

---

## 3. The theory being formalised

*Aperture inexternalism* (owner framework, tier H — not scripture, not
peer-reviewed literature):

> One conscious subject is one concrete, causally active process, described
> extrinsically as an embodied aperture and existing intrinsically as a private,
> valenced phenomenal field.

Its central identity is written `D_i ≡_inext O_i*`: one phenomenal field is
numerically identical with one objectively individuated aperture process, under
two modes of access. The framework rejects both "experience is produced by an
unconscious mechanism" and "experience floats free of physical causation".

By §2 this is a **layer-D** theory with a layer-A inventory attached (nine named
aperture operations, owner spec v0.7).

---

## 4. The encoding (Lean 4.34.1)

### 4.1 Layer A — inventory

```lean
def apertureOps : List String :=
  ["manifestation", "retention", "determination", "stream-integration",
   "counterfactual-generation", "value-weighting", "finite-possibility-space",
   "cross-stream-boundary", "inter-stream-influence"]

theorem aperture_nine : apertureOps.length = 9 := by decide
theorem aperture_distinct : apertureOps.Nodup := by decide
```

Two propositions, both `by decide`. No semantics is imported: the file header
states that the roster is a list of functional *tags*, not a theory of
experience, and that individuation is untouched.

### 4.2 Layer B — the operation

```lean
inductive Sigma | instrument | primary

structure Field where
  knower : String
  world : String
  relation : String
  sigma : Sigma

def recognise (f : Field) : Field :=
  { f with sigma := (match f.sigma with
                     | .instrument => .primary
                     | .primary => .instrument) }
```

Twelve theorems in the core file (six operation, two invariance, two exclusion, two positioning inventory) plus a Z/2 action layer (eight theorems: group laws, action laws, content invariance, generator agreement, involution from the group law) and a cut result (no cross-block flow):

| Theorem | Statement | Method |
|---|---|---|
| `sigma_two` | exactly two positionings | `decide` |
| `sigma_distinct` | the two are distinct | `decide` |
| `recognise_preserves_content` | knower, world, relation unchanged | `simp` |
| `recognise_changes_positioning` | σ changes (not the identity) | case split |
| `recognise_involution` | recognising twice returns the field | `rfl` |
| `mode_switch_preserves_content` | the two modes of access carry the same content | `decide` |
| `sample_no_production` | no transition in the model produces a state (exclusion C1) | `decide` |
| `sample_one_process` | extrinsic redescription is the identity on every field (exclusion C2) | `decide` |

The last one is the formalisable heart of the identity theory: the claim that
switching mode of access changes *nothing* about the process, only how it is
described. That is a real claim and it is checkable.

### 4.3 Layer D — what is deliberately absent

There is **no theorem named `identity`**, no `theorem experience_is_process`, and
no definition that makes the phenomenal field and the aperture process the same
term. The file header says so explicitly. Encoding the identity as a definition
of one carrier with two projections is legitimate; proving it is not, because the
two descriptions are not the same object in the formalism and pretending
otherwise is the identity inflation of §1.3.

### 4.4 The twin (the instrument must bite)

```lean
-- BrokenInexternalism.lean: the only change is in reDescribe
def reDescribe (f : Field) : Field :=
  { f with world := f.world ++ "-seen" }
```

`tools/must_fail.py` compiles the mutant and *requires* exactly one error, at the
proposition `mode_switch_preserves_content`, with Lean reporting that `decide`
proved it false. A vacuous checker would let the mutant through. It does not.

The twin is not decoration. It is the only evidence that layer B is being
tested rather than merely type-checked.

---

## 5. What was and was not established

**Established (machine-checked, inside the finite model):** the inventory is
finite and distinct; the operation preserves content; it changes positioning; it
is an involution; the sample is closed; the mode switch preserves content.

**Not established, and stated in the file:** that a phenomenal field *is* an
aperture process; that the nine operations are exhaustive of experience; that any
particular subject is individuated by them.

**On the strength of the check.** The corpus this encoding belongs to contains 57
hand-written twins, each of which the checker must refuse. That is a
**non-vacuity** argument: the instrument bites. It is *weaker* than a soundness
or faithfulness theorem, and this paper does not present it as one. Two adjacent
projects in the same tradition — a cubical type-theoretic formalisation of
Navya-Nyāya and an axiomatic formalisation of Advaita Vedānta — do carry
metatheory and explicit limitations respectively; the honest position here is
"no soundness claim; a non-vacuity claim; here is the twin that would have caught
a vacuous checker".

---

## 6. The method, generalised

For any theory with an identity at its core:

1. **List the inventory.** Names only, no semantics. One theorem: finite and
   distinct.
2. **State the operation.** What changes, what does not. Prove preservation and
   variance separately. This is where most of the real content lives.
3. **Encode the exclusions.** "Experience is not produced", "experience does not
   float free" become predicates with a stated domain and a proof that the
   theory's own operations cannot derive the excluded case.
4. **Define the identity; do not prove it.** Exhibit one model in which it holds,
   derive two consequences, and name one alternative it rules out.
5. **Declare the primitive.** Phenomenality, valence, or whatever else resists
   formalisation, is declared at the top with a tier and never appears in a
   conclusion.
6. **Write the twin.** One definition changed, one named proposition falsified,
   and a gate that refuses to accept a generic compile error.

Step 6 is the difference between a formalisation and a diagram.

---

## 7. Limitations

- One worked example, chosen by the authors. Generality is argued, not shown
  across multiple theories.
- The corpus is H-tier owner theory: the encoding's fidelity is to a written
  framework, not to a text or a peer-reviewed paper.
- The finite model is a model of a *description*, not a simulation of cognition.
- No empirical claim is made and none could be: layer B theorems constrain
  descriptions, not subjects.
- The comparison literature is recorded as published and was not re-verified in
  the same session as the proofs.

---

## 8. Conclusion

Identity theories can be formalised honestly, but what gets proved is narrower
than their authors usually want: the inventory, the operation, and the
exclusions — not the identity. Naming that boundary in the artefact, and writing
a twin that forces the checker to bite, converts a metaphysical essay into
something a sceptic can inspect. That is the whole contribution, and it does not
require a single new theorem about consciousness.

---

## Submission shape (proposal, not a submission)

**Target, in order:**

1. ***Neuroscience of Consciousness* (Oxford, open access).** Publishes formal
   + philosophical work (e.g. the Prueitt et al. bridge paper this method
   follows), accepts negative and methodological results, and reaches the
   consciousness-science audience the comparison programme needs.
2. ***Journal of Consciousness Studies*.** More theoretical, weaker on formal
   apparatus; a fallback if reviewers want the philosophy without the Lean.
3. ***Synthese*.** Strong for the formal method, weaker for the
   consciousness-studies readership. Third choice.

**Abstract (198 words, draft).**

> Formal theories of consciousness are rarely checked against anything. We
> propose a five-layer decomposition that makes the checkable part of an
> identity theory explicit: inventory, operation, exclusion, identity,
> phenomenality. Only the first three are formalisable; the identity is a
> definition with consequences, never a theorem; phenomenality is a declared
> primitive. We work the method on aperture inexternalism — the claim that one
> phenomenal field is numerically identical with one objectively individuated
> aperture process — encoded in Lean 4. The core file carries ten theorems
> (content preservation, involution, mode-switch invariance, two exclusions);
> a second file proves the flip is the generator of exactly Z/2 and derives
> involution from the group law; a third proves recognition dynamics carry no
> cross-block flow (the Phi = 0 case, without a Phi definition). No theorem is
> named for the identity. A hand-written twin corrupts the mode switch so it alters
> content, and the checker is required to refute a named proposition; it does.
> Non-vacuity, not soundness, is the claim — 62 such twins, weaker than
> metatheory and presented as such. The method transfers to any theory with a
> metaphysical identity at its core: list the inventory, state the operation,
> encode the exclusions, define the identity, declare the primitive, and write
> the twin that would catch a vacuous formalisation.

**What the paper needs before submission:** a venue decision by the owner, a
named human signature on the identity-limitation paragraph, and a re-read of
the full Yan et al. (2026) article once accessible.

---

## References

**Verified in-session (2026-11-17):**

- Prueitt, C., Sezer, I., Sacchet, M. D. (2025). Reimagining pain as an
  allostatic imperative. *Neuroscience of Consciousness* 2025(1): niaf049.
  doi:10.1093/nc/niaf049.
- Berwian, I. M., Hitchcock, P., Pisupati, S., Schoen, G., Niv, Y. (2025).
  Using computational models of learning to advance cognitive behavioral therapy.
  *Communications Psychology*. doi:10.1038/s44271-025-00251-4.
- Smith, R., Moutoussis, M., Bilek, E. (2021). Simulating the computational
  mechanisms of cognitive and behavioral psychotherapeutic interventions.
  PMC8115057.
- Mansell, W., Huddy, V. (2020). Why do we need computational models of
  psychological change and recovery. *Frontiers in Psychiatry*.
  doi:10.3389/fpsyt.2020.00624.
- Schiepek, G., Aas, B., Viol, K. (2016). The Mathematics of Psychotherapy.
  PubMed 27262423.
- Bhattacharyya et al. (2026). Cubical Type Theoretic Navya-Nyāya.
  arXiv:2605.12548.
- Chapman, C. (2026). The Modal Catuṣkoṭi. *Comparative Philosophy* 17(2): 4–17.
  doi:10.31979/2151-6014(2026).170205.
- Roy, S., Posina, V. R. (2024). Category Theory and the Ontology of Śūnyatā.
  doi:10.1163/9789004691568_026.
- Tavva, R., Singh, N. (2015). Generative Ontology of Vaiśeṣika. CEUR-WS
  Vol-1517.
- Fujimoto, N. (2026). Nāgārjuna's Empty Vessel: A Lean 4 Axiom-Free Formal
  Encoding. doi:10.5281/zenodo.20838891.
- Scherf, M. Advaita Vedānta: A Formal Axiomatization (Lean 4).
  github.com/matthew-scherf/Advaita/ (repo verified live 2026-11-17; Zenodo doi:10.5281/zenodo.17333604).
- Yan, T. et al. (2026). Formalizing consciousness: a comparative mathematical
  analysis of leading theories. *Biological Cybernetics*.
  doi:10.1007/s00422-026-01068-y. **Read as abstract + metadata + companion
  papers only; the full text is paywalled and was not read. Method reconstructed,
  not cited as read.**
- Kirchhoff, M. et al. (2018). The Markov blankets of life. *J. R. Soc.
  Interface*. PMC5805980.

**Standard references, not re-verified in-session:** Rosenthal (higher-order
thought); Tononi and colleagues (IIT); Baars / Dehaene and colleagues (global
workspace); Johnson and colleagues (QRI symmetry theory).
