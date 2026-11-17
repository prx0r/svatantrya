# IMPORT — Yan, Tsukahara, Williford, Rudrauf & Sergeant-Perthuis (2026)
## "Formalizing consciousness: a comparative mathematical analysis of leading theories"

*Status: REFERENCE IMPORT. What we read, what we took, what changed in trika-x as
a result. (2026-11-17.)*

---

## 1. The artefact

- **Journal:** *Biological Cybernetics*, Original Article, published 14 Nov 2026.
- **DOI:** `10.1007/s00422-026-01068-y`
- **Preprint:** HAL `hal-05586345v1` (2026-04-09).
- **Authors:** Tonglin Yan (Paris-Saclay), Jules Tsukahara (IMJ-PRG), Kenneth
  Williford (UT Arlington), David Rudrauf (Paris-Saclay), Grégoire
  Sergeant-Perthuis.

**What we actually read (honesty note).** The Springer full text is paywalled
and JS-gated; HAL serves an Anubis proof-of-work challenge. We read: the full
abstract and metadata (Springer + HAL), the companions the paper builds on —
*Integrated Information Theory (IIT) with Simple Maths* (HAL `hal-04531404`),
*The Projective Consciousness Model and Phenomenal Selfhood* (Front. Psychol.
2018;9:2571), *Projective Geometry at the Core of Consciousness* (Brain Sci.
2023;13(10):1435), and *Why the PCM must be true* (Rudrauf & Pansu preprint) —
and reconstructed the method from those. **The method below is therefore a
faithful reconstruction, not a citation-grade summary of the full article.** Any
paper citing it must read the published version.

---

## 2. Their method, in five moves

1. **Compare at Marr's computational and algorithmic levels, not the
   implementation level.** Most theory clashes in consciousness science are
   level mismatches dressed as contradictions.
2. **Build one shared mathematical language** from probability theory,
   information theory and geometry: probability spaces and Markov kernels,
   conditional independence, information measures, group actions and geometric
   structures.
3. **Reformulate each theory's core mechanism in that language** — IIT (cut and
   integrate), GWT (compete and broadcast), AIF (minimise expected free energy),
   HOR (meta-represent), PCM (project the world model through a viewpoint).
4. **Inventory shared tools, scope, and tractability.** Say which tools two
   theories share, which explanatory question each answers, and whether the
   quantity is computable — Φ is exponential in the worst case; broadcasting is
   simulation; geometry is continuous optimisation.
5. **Propose a common testbed agent** in which integration, broadcasting,
   higher-order access and perspectival transformation are all available, so
   theories can be compared inside one architecture.

The paper's own strongest example of step 1: IIT and AIF look incompatible until
you notice that one asks what a system's causal structure is and the other asks
what an agent must do under uncertainty.

---

## 3. What we took (and changed in the code)

### T1 — Scope discipline (the big one)

`tools/compare.py` now requires a `scope` of `same` or `different`, and **an
`incompatible` verdict is only legal when the scope is the same.** A different
explanatory question is a new verdict: `not-comparable`, which must name the
`scope_difference`.

Reclassification this forced:

| Record | Was | Now | Why |
|---|---|---|---|
| HOT (Rosenthal) | incompatible | **not-comparable** | HOT explains what makes a *state* conscious; trika-x describes self-positioning. Different question. The additivity clash remains recorded as a disparity, not as a contradiction |
| QRI valence | incompatible | **not-comparable** | QRI asks for a valence geometry; trika-x has an inventory of aesthetic modes. Different question |

This is a real correction to our map: two of our six "incompatibilities" were
scope mismatches. Four survive with the same scope and a missing signature.

### T2 — Shared-tool inventory

Every record now names the formal tools the comparison needs
(`shared_tools`): Markov kernel, conditional independence, Φ; competition and
capacity bound; state ontology and meta-relation; group action; cubical
negation. The obstruction becomes mechanical: **a signature mismatch is a
missing tool**, not an opinion.

### T3 — Tractability

Every record states both sides' computational class. Ours is
`O(n) enumeration (by decide) over finite tables`; theirs range from exponential
(IIT) to continuous optimisation (PCM) to simulation (GWT). This makes a claim we
could not previously make: **trika-x's verification is cheap and its object is
small; the field's theories are expensive and their object is large.** Our
comparative advantage is containment, not coverage.

### T4 — The testbed idea (not yet built)

Their common testbed is the right shape for our gaps: one finite carrier with
optional layers — a Markov kernel (enables Φ), a broadcast step (GWT), a
meta-relation (HOT), a group action (PCM). Each theory becomes a flag on the same
carrier, and the "missing signature" obstructions become "layer not installed".
Recorded as W11 below; **not** built in this session.

### T5 — We found our nearest neighbour, and had missed it

The paper's fifth theory — the **Projective Consciousness Model** — was absent
from our ten comparisons. It should not have been. PCM writes:

> `S(X,t) = T(t) ∘ R(X,t)` — subjective experience is a world model `R`
> transformed by a projective transformation `T` (viewpoint), with viewpoint
> changes acting as collineations in `PGL(4,R)`.

That is **exactly** our content/positioning separation: `R` is content, `T` is
positioning, and our theorem `mode_switch_preserves_content` says the mode switch
changes nothing about the content. Trika's σ-flip is the **two-element degenerate
case** of their group action.

New record `pcm-projective-perspective`, verdict `partial` — the strongest
mapping in the corpus:

- shared: content/positioning separation; change is a transformation of access;
  experience is perspectival by construction.
- disparity: they **derive** the group from four perceptual postulates; we
  **stipulate** two values. Ours is weaker and more general; theirs is stronger
  and narrower.
- upgrade path: generalise `Sigma` to a group acting on the field, recover the
  two-element flip as the degenerate case, and prove content invariance for the
  action. **That would change the verdict to `fit` and strengthen both sides.**

---

## 4. What we did not take

- Their theory selection (IIT/GWT/AIF/HOR/PCM) is a theory-of-consciousness
  selection; our unit is a *tradition's structural commitments*. We borrow the
  method, not the roster.
- No proof assistant, no provenance, no source binding in their work. Our
  contribution is the opposite trade: small formal objects, hard provenance.
- We do not adopt their claim that apparent disagreements are *mostly* level
  differences. Our reclassification moved two of six. The rest are genuine
  signature clashes.

---

## 5. What this means for the papers

- **P1** gains a paragraph: Marr-level discipline is why an identity theory must
  declare which level it speaks at, and why layer E (phenomenality) is not an
  implementation claim.
- **P2** changes materially: verdicts are now
  `4 incompatible · 4 partial · 1 fit · 2 not-comparable`, and §5 must explain
  that "not-comparable" is a finding, not a failure.
- **P2** gains PCM as its strongest positive result — the one place where the
  Trika structure and a leading formal model share a formula shape
  (`S = T ∘ R` vs content-invariance under the mode switch).

---

## 6. Honest assessment of the import

The most useful thing this paper did was **weaken two of our own verdicts**. That
is the correct outcome of importing a method: it should be able to correct you.
The second most useful thing was surfacing PCM, which turns our best negative
map into a possible positive bridge.

The risk it creates is **level laundering**: with a `not-comparable` category, a
lazy comparison could dump every hard case there. The guard is that
`not-comparable` must name the different explanatory question, and `incompatible`
requires the same scope — so the classification cannot absorb an unexplained
failure.

---

## 7. Verification checklist for anyone citing this import

- [ ] Read the published article (DOI above). This note is a reconstruction.
- [ ] Check whether their "common testbed" has been implemented since.
- [ ] Re-check the PCM necessity claim (Rudrauf & Pansu preprint) before
      repeating "RP³ is necessary given P1–P4".
- [ ] Confirm `PGL(4,R)` is the right group for the Trika generalisation before
      writing it as anything but a proposal.

---

## 9. Citation verification log (2026-11-17)

The search layer returned two 404s that turned out to be **fetcher quirks, not
fabrications** — and the check forced a canonical-URL discipline into the
records. Results:

| Item | Status | Evidence |
|---|---|---|
| Advaita Lean repo (Scherf) | **VERIFIED**, multi-source | repo page resolves (trailing slash), Zenodo doi:10.5281/zenodo.17333604, SuttaCentral discussion; Lean v4.12.0, MIT, 129 axioms confirmed |
| Chapman modal catuṣkoṭi | **VERIFIED**, multi-source | SJSU scholarworks full text (Vol 17 No 2, pp 4–17), GitHub repo rollofthedice/modal-catuskoti-lean exists, author Substack confirms peer review; DOI resolver 404 was a resolver quirk, canonical URL is the scholarworks page |
| arXiv:2605.12548 (cubical NN) | **VERIFIED**, fetched-primary | abs page: cs.LO, 10 May 2026, authors/abstract match |
| arXiv:2511.05580 (psychodynamics SMC) | **VERIFIED**, fetched-primary | abs page + PDF content: Bagley & Khoshnan, SMC/process theory, cogits confirmed |
| arXiv:2509.02144 (AI therapy) | **VERIFIED**, fetched-primary | abs page: Herbener & Damholdt, genuineness/credibility gaps confirmed |
| Prueitt/Sezer/Sacchet 2025 | **VERIFIED**, fetched-primary | PMC12687940, PMID, DOI, Harvard-hosted PDF; heterostatic/homeostatic distinction and the "not allostatic imperativists" disclaimer confirmed verbatim |
| Fujimoto Zenodo 20838891 | **VERIFIED**, multi-source | Zenodo record + author blog; **caveat**: independent researcher + AI substrate, self-published — cited for the verification-boundary practice, not as peer review |
| Tavva & Singh JOWO 2015 | **VERIFIED**, multi-source | CEUR Vol-1517 PDF + researchr + JOWO program + author pages |
| Roy & Posina 2024 | **VERIFIED**, multi-source | NIAS record + ResearchGate abstract + Scholar cites; Brill chapter pp 450–478 |
| Yan et al. 2026 | **ABSTRACT ONLY** | full text paywalled/JS-blocked; method reconstructed, marked as such everywhere it is cited |
| HOT / IIT / GWT / QRI | **STANDARD, not re-fetched** | textbook-level claims; re-fetch before any submission |

Enforcement added to `tools/compare.py`: every record needs
`citation {sources, verified date, method}`; `fit` requires fetched-primary or
multi-source; a `not-comparable` or `standard`-only record is legal but flagged.
Verification is now a gate, not a hope.
