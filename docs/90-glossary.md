# 90 — Glossary
*Status: REFERENCE. Layers, tiers, verdicts, roles, terms. (2026-11-14.)*

## Layers (public name → machine key)

| Public name | Key | One line |
|---|---|---|
| source | SOURCE | The sha-pinned Sanskrit bytes. Never translated, only cited. |
| draft-translation | T1 | Fast pass: verse draft + quick gloss per token. |
| literal-gloss | L0 | Term-by-term audit; meaning-forks live here and nowhere else. |
| argument-map | ARGMAP | The verse as a whole: speaker, premises, inference, payoff, uncertainties. |
| reading-translation | L2 | Our translation proper, clause-traced to literal-gloss ids. |
| essence | C1 | The sharpest poetic reading of what the verse DOES. |
| register-render | C2 | Register rendering + reproducing prompt/model/paragraph maps. |
| final-translation | L3 | One translation to look at, frozen once loved. |
| song | L4 | The final translation set to music. Requires L3. |

Keys never change (everything keys on them); names are additive, either accepted
on input.

## Tiers

**T** root text · **R** reconstruction (never promotes itself) · **E** empirical ·
**C** correspondence · **H** hypothesis · **X** rejected.

## Verdicts

- **COMPLETE** — every applicable hop bound/passed/checked.
- **PARTIAL** — named unknowns; never shipped as settled, never signed.
- **BLOCKED** — a gate stopped the chain; recorded with the reason.
- **UNRESOLVED / CANDIDATE / UNPINNED** — valid identity states, never silently promoted.

## People and roles

- **Owner** — holds the switches: OAuth, tokens, Zenodo, witnesses, indexing,
  consent, disk, dīkṣā policy. Only the owner publishes, signs, or ships.
- **Lanes** — repo-owning builders (translation-work ingest, svread surface,
  factories, nibbanahelp). Read-only to each other; specs, never cross-writes.
- **Scholar** — human review/signoff channel (P-TK1 rulings, rater-2, ti/ca).
- **Agent** — machine that proposes, tests, receipts, and never disposes.

## Key terms

- **Trace bundle** — one chunk's full chain: source bytes → layers → proofs →
  theorems → citing essays, with a COMPLETE/PARTIAL verdict.
- **Must-fail twin** — a hand-mutated Lean file the checker is required to
  refuse; proves the checker bites, not just compiles.
- **Run receipt** — Lean version + command + file sha + exit code + seconds;
  provenance for generated certificates.
- **PUSHBACK** — cross-model destroy pass over a draft; report, never a verdict.
- **Treeka** — the argument graph: works → passages → argmaps → cruxes →
  essays, plus the gap report that queues the next rung.
- **FailOpen** — a dead MCP child is excluded from tools/list, never fatal.
- **Read sheaf** — the public, no-auth tool subset. Writes need OAuth (unissued).
