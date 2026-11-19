# Flaws and obstacles — the steelman against this project
*Status: CANONICAL. Read before citing any result from this estate. (2026-11-17.)*

*This document exists because the project's own discipline demands it: every
claim carries its denominator, and the project itself is a claim. Nothing here
is a confession for effect; each flaw names what would fix it and whether that
fix is in anyone's power.*

---

## Flaws (internal; ours to fix or own)

### F1. The theorems are true by construction
`by decide` over a finite list proves the list has the stated property. The
list is ours. So nearly every theorem in the corpus is a tautology over our own
definitions. The only epistemic content in the whole Lean corpus is: (a) the
definitions match their claimed sources — a human judgment, currently
unreviewed; (b) the checker works — established by twins. Anyone presenting a
`decide` theorem as a discovery is misrepresenting what happened. The
discoveries that *are* real (the Z/2 characterisation, the fourth-lemma trade)
came from the *structure* of the encoding, not from any proof — and must be
described that way.

**Fix:** the grounding check (§W below) closes (a) at the locator level; (b) is
closed by twins. Nothing closes the gap between "the table is consistent" and
"the table is true of the text" except a scholar reading both.

### F2. No soundness, no faithfulness, no completeness
Stated in `SOUNDNESS.md`, repeated here because it is the load-bearing weakness:
there is no theorem that any encoding means what it claims. The cubical
Navya-Nyāya work has all three; we have none. Our substitutes — twins and
scope notes — are weaker and must never be dressed as equivalents.

**Fix:** none cheap. A soundness statement needs a semantics; we have not
defined one. Do not claim progress here until one exists.

### F3. Owner theory sits in the same registry as tradition
H-tier rows (aperture, inexternalism, testbed) live in `EVIDENCE.json` next to
T-tier rows (kancuka counts from the Tantrasāra). Tiers label the difference,
but a careless reader — or a future agent — can still cite an H row as if it
were textual. The registry's uniformity is a laundering risk.

**Fix:** done in part — `kind: MODEL` + `r_sources` name the owner framework on
every H row. Remaining: the Scholar surface should render H rows with a visible
badge. Not yet built.

### F4. Witnesses: zero
Every T-tier claim is pinned to an edition that is itself a candidate string.
`UNPINNED` is stated, but downstream language ("VERIFIED-QUOTE",
"ARGMAP-PINNED") sounds stronger than its foundation. A hostile reviewer needs
exactly one sentence: *verified against what manuscript?*

**Fix:** owner-held (manuscript access). Until then, every paper must carry the
limitation in §1, not §8.

### F5. Coverage is 10% and biased toward the countable
16/154 passages, and the 16 are the ones with enumerable structure (counts,
orderings, tables). Nothing about the hard parts — recognition as an event,
grace, the aesthetic claim — is formalised, because those resist enumeration.
The corpus therefore over-represents what Lean finds easy. Any aggregate claim
("trika-x formalises Trika") must carry the denominator and the bias note.

### F6. The comparisons rest on secondary readings
With one exception (Prueitt et al., read in full), our characterisations of HOT,
IIT, GWT, QRI, Advaita-as-formalised, and the rest come from abstracts,
textbooks, and code READMEs. The verdicts are structural and checkable, but the
*inputs* to the structures are unreviewed summaries. A specialist in any one of
these traditions could overturn a verdict by correcting our description of
their side.

**Fix:** verdict review (W1) must include, per record, "is the other side
fairly stated?" as a separate question from "does the mapping hold?".

### F7. No users, no signers
`core: 0`, `UNREVIEWED` everywhere, zero external users of the MCP surface that
we know of. A provenance machine with no provenance flowing through it is a demo.

### F8. The generated essays are thin
Nine claims from a template, sections derived one-to-one from the record. They
pass the gate because the gate checks structure, not thought. A reviewer will
notice the formula on the second essay. Generated essays are scaffolding for a
human draft, not drafts.

### F9. One box, one tunnel, pasted tokens
The live surface depends on a single machine, a Cloudflare tunnel, a shared
bearer in `/etc`, and a pasted GitHub token. This is an ops posture, not an
infrastructure. Token rotation is owner-blocked and overdue.

### F10. The "testbed" is one proposition
`testbed_joint` checks dynamics + action on four indices. Calling it a common
testbed overstates by an order of magnitude: no docking layer exists, no second
theory has been mounted on it, and the joint check is a conjunction, not an
architecture.

### F11. The AI analysis is conceptual, not tested
Sycophancy and syncretism as structural disqualifiers, the mirror argument,
the "informational ≠ relational advantage" claim — none has an experiment. F5
in THESIS needs an IRB and a partner, not more prose.

### F12. Apologetics risk
A project that formalises one tradition, run by its adherents, reads as
apologetics with a proof assistant — especially with Vivekananda in the
framing. The mitigations are real (tiers, negative verdicts, stated
limitations) but the risk is reputational and cannot be discharged internally.
External reviewers from *outside* the sympathetic traditions are the only fix.

---

## Obstacles (external; not ours to fix alone)

| # | Obstacle | What unblocks it |
|---|---|---|
| O1 | No engaged scholar will sign a claim | one Indologist on one chapter; offer co-authorship, not tooling |
| O2 | No manuscript witnesses | NGMPP/microfilm access; owner-held |
| O3 | No natural venue: too formal for humanities journals, too philosophical for formal venues, too niche for consciousness science | the Yan et al. paper proves the venue exists; P1 targets it first |
| O4 | The literature moves faster than the records | the citation gate (verified dates) at least timestamps the decay |
| O5 | No lane chosen: scholar tool, agent API, learner product, personal endgame — all half-built | owner decision; building continues to diffuse until then |

---

## What this document changes

Nothing is hidden that was previously shown, but three things are now explicit
policy:

1. `by decide` theorems are never cited as discoveries. Discoveries are the
   characterisation results (Z/2, fourth-lemma trade, Advaita disparity) and
   must be described as structural, not proved.
2. Every comparison with a `standard`-only citation carries that fact into any
   essay generated from it.
3. F4 goes in §1 of every paper, not the limitations section.

*The project is a machine for making checkable claims. This file is the machine
checking itself.*
