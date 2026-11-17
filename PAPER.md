# What this actually is
*Status: CANONICAL. Public-facing paper: what this actually is, for an intelligent outsider. (2026-11-14.)*

*A public paper about the Svatantrya estate. No prerequisites assumed beyond
curiosity. Every number below was produced by running the command beside it on
2026-11-14; nothing here is a roadmap item dressed as a result. Where something
is not yet done, it says so in plain words.*

## The one-paragraph version

Svatantrya is a machine for answering hard questions about Sanskrit Trika texts
**in a way you can check**. Ask about a verse and you get Sanskrit bytes with a
hash, every translation layer that touches it, a machine-checked formal model
of what the verse claims structurally, and an essay trail — or, where the chain
breaks, an honest label saying so (`PARTIAL`, `UNVERIFIED`, `UNKNOWN`). It
proves what machines can prove, labels the rest, and never presents a model
output as scholarship. The whole thing is live and queryable today, including
from ChatGPT.

## The problem it solves

AI answers about Sanskrit philosophy are fluent, confident, and very often
wrong in ways you cannot detect — a misattributed verse, a smoothed-over
ambiguity, a doctrine stated as fact that no edition supports. The failure is
not that models hallucinate; it is that **nothing records provenance**: which
text, which edition, which bytes, which human signed off.

Svatantrya inverts the economics. Generation is cheap and stays cheap. What the
estate manufactures, expensively and on purpose, is **provenance**: a
hash-pinned trail from any claim back to source bytes, with a machine-checked
step where machines can check and a named human where they cannot.

## How it works: one question, one chain

```
Which text is this?          → openpatala resolves work/edition (UNRESOLVED = draft-only)
What does the verse say?     → translation layers: draft → literal gloss (forks live here)
                                 → argument map → reading translation → essence → final → song
Does the structure check out?→ Lean theorems: counts regenerate, twins refuse to compile
Can I see the whole trail?   → trace bundle: source bytes + layers + proofs + theorems
Who stands behind it?        → essay claims → audit → cross-model pushback → HUMAN signs
```

Each arrow is the same contract: **bytes + hash + status + where to re-fetch**.
A hop that cannot name its input fails closed. Missing data is `UNKNOWN`, never
filled in by analogy or by a model guess.

The translation layers deserve one sentence each, because they are the heart of
it: the *literal gloss* records every genuine meaning-fork as a ranked option
with grammatical grounds (forks live here and nowhere else); the *argument
map* reads the verse as a whole and adjudicates those forks on the record; the
*reading translation* renders it in plain English with every clause traced back
to the gloss. Nothing downstream may invent what the gloss does not contain.

## What the machine actually proves

In `trika-x/formal-trika`, Lean 4.34.1 checks finite models of traditional
doctrine — counts, orderings, gatings. Not interpretations; arithmetic.

| Check | Result | How verified |
|---|---|---|
| Lean control models | **53 PASS / 0 FAIL** | `sh formal-trika/control/run.sh` |
| Lean recognition models | **26 passed / 0 failed** | `sh formal-trika/recognition/run.sh` |
| Evidence registry | **225 theorems · 165 entries · 2 exemptions · 1 generated · 0 problems** | `tools/evidence_check.py` |
| Coverage | **16 of 154 chunks (10%)**, gap list published | same command |
| Axiom hygiene | **CLEAN** — no `sorry`, no smuggled axioms | `tools/axiom_audit.py --check` |
| Full test suite | **132 tests OK (1 skipped)** | `python3 -m unittest discover -s formal-trika/tests` |

The number that matters most is not 206. It is the twins: every theorem ships
with a hand-written mutant — a single-definition corruption — that the checker
is **required to refuse**. If the checker were vacuous, the mutant would
compile; it does not, 57 times over. That is what "machine-checked" means
here: the instrument bites, and we prove that it bites.

And the number that matters second-most is 10%. Sixteen of 154 passages are
formalized. The gap list is published, the queue is worked in order, and no
one will tell you coverage is higher than it is.

## How honesty is enforced, not just claimed

Five rules are load-bearing, and the tooling enforces them rather than asking
nicely:

1. **Tiers on every claim** (T root text, R reconstruction, E empirical, C
   correspondence, H hypothesis, X rejected). A reconstruction may never
   promote itself to root text — not by a model, not by an agent, not ever.
2. **BLOCKED is never PASS.** Timeouts, empty responses, and upstream failures
   are errors. A gate that cannot run reports `BLOCKED` with the reason.
3. **No rung ships without hash, grounds, gate, and signer.** The 49
   generated certificate theorems in the count above are not evidence rows:
   each is bound to a receipt (file sha + pack sha + Lean version + exit
   code), and the checker fails closed if any binding breaks.
4. **Machine proposes, human disposes.** No auto-sign, no auto-publish, no
   auto-push. Any pipeline step that would publish, promote, or spend requires
   an explicit owner go.
5. **Private stays private.** Diary material ships only with explicit, scoped,
   revocable consent. There is no bulk path from a person's journal to the
   public, by design.

## What you can use today

No account, no code, from the open internet:

- **Read the library**: [svatantrya.net](https://svatantrya.net) — reader,
  Sanskrit lessons, practice wheels, bibliography, scholar projections.
- **Ask the formal layer** (no auth):
  ```sh
  curl -s -X POST https://formal.svatantrya.net/mcp \
    -H 'Content-Type: application/json' \
    -d '{"jsonrpc":"2.0","id":1,"method":"tools/call",
         "params":{"name":"formal__trace",
                   "arguments":{"work":"tantrasara-a08","target":"tsa08-p03"}}}'
  # → verdict COMPLETE, 9 Lean theorem rows with registry status
  ```
- **Browse the public bundle** (`https://mcp.svatantrya.net/mcp`, 51 tools):
  resolve a work, pull passage evidence with layer hashes, walk the treeka
  argument graph, run a Sanskrit wheel.
- **Use it from ChatGPT**: the "Svatantrya" plugin exposes the public bundle;
  the owner console (`mcp.sanskrit.help`, 210 tools) is bearer-gated.

909 trace bundles back every served passage; 236 are COMPLETE and 673 are
PARTIAL, each PARTIAL naming exactly what is missing.

## What it is not (stated plainly)

- **Not a translation authority.** Machine translations are labeled
  machine-proposed until a human scholar signs them. The sign-off queue is
  real and mostly empty — that is honest, not broken.
- **Not a guru.** Nothing here authorizes practice, initiation, or teaching.
  Practice tooling is study-only until the dīkṣā policy owner decides otherwise.
- **Not complete.** Formal coverage is 10%. There are zero verified manuscript
  witnesses — editions are candidate strings, and the resolver says
  `UNPINNED` rather than inventing sigla.
- **Not finished.** The diary→essay→audio→video→book recipe family exists as a
  spec with a working essay pipeline; the consent-gated end-to-end path is
  owner-gated and deliberately unbuilt until the owner opens it.

## The parts (one line each)

| Part | Role |
|---|---|
| **OpenPāṭala** | Identity: which work/edition/passage is this (1034 works, 909 passages) |
| **translation-work** | Evidence: the eight translation layers, per chunk, sha-pinned |
| **trika-x / formal-trika** | Proof: Lean models, twins, traces, the federation gateway |
| **svread** | Surface: reader site, scholar evidence, public MCP gateway |
| **nibbanahelp** | Person: diary, tensions, relay (private by construction) |
| **bookfactory / videofactory** | Render: gated books and videos (nothing ships ungated) |
| **sanskritbench / ipvv / satsang / deitybody** | Calibrate, translate, directory, body-curriculum |

## Where this goes

The direction is fixed and the scope is honest: climb formal coverage rung by
rung (each rung preregistered, twin-tested, human-signed); keep every public
surface reading only from gated outputs; open the diary→teachings→media
recipes one consent-gate at a time, starting with the personal essay. Nothing
here needs a breakthrough — it needs scholars, witnesses, and time. The
machine's job is to make sure that when they arrive, everything they touch is
checkable.

*Machine proposes, human disposes. BLOCKED is never PASS. Counts carry
denominators or they don't ship.*
