# Svatantrya — the Trika endgame, documented from the ground up

> One question about a Trika text walks down to a witness and back up to a
> signed, DOI'd essay — or a lesson, or a practice — with every link
> hash-pinned, decision-tracked, gate-checked, and machine-verified where
> machines can verify. **Commodity generation; scarce provenance.**

This repo is the complete documentation for the whole estate: the thesis, every
layer, every repo, the live state, and what "finished" means. Start here, then
follow the map. Nothing here invents numbers — every count carries the command
that produced it.

## The spine (one diagram)

```
witness → chunk → layers → formal → arguments → treeka → essay → teacher/agents/practice
   │         │         │         │          │          │        └─ nibbanahelp · satsang · deitybody
   │         │         │         │          │          └─ Scholar (svread + translation-work)
   │         │         │         │          └─ pushing corpus (ipvv) → treeka
   │         │         │         └─ formal-trika Lean proofs (trika-x)
   │         │         └─ translation-work layers: draft → gloss → argument → reading → essence → register → final → song
   │         └─ translation-work passages (chunk locators, immutable ids)
   └─ openpatala: Work → Edition → Witness → Surrogate → EText (identity root)
```

## Map

| Doc | What |
|---|---|
| [docs/00-thesis.md](docs/00-thesis.md) | The goal, the laws, the tiers — why this exists |
| [docs/10-openpatala.md](docs/10-openpatala.md) | Identity: the scholarly state machine (live: 1034 works) |
| [docs/20-translation-evidence.md](docs/20-translation-evidence.md) | Evidence: translation layers, Scholar, claims, audit |
| [docs/30-formal-proofs.md](docs/30-formal-proofs.md) | Proof: Lean spine, what is machine-checked (53+26, 206 theorems) |
| [docs/40-federation-mcp.md](docs/40-federation-mcp.md) | Access: one MCP federation, ChatGPT plugins, read sheaf |
| [docs/50-recipes.md](docs/50-recipes.md) | Endgame: diary → teachings → media → journey (R1–R9) |
| [docs/60-live-state.md](docs/60-live-state.md) | Verified live endpoints, counts, receipts (2026-11-14) |
| [docs/70-v1-tracker.md](docs/70-v1-tracker.md) | V1 definition of done + repair queue |
| [docs/80-methodical-checklist.md](docs/80-methodical-checklist.md) | Methodical verification, one step at a time — Step 1 (trika-x) done |
| [docs/90-glossary.md](docs/90-glossary.md) | Layer names, tiers, terms |
| [docs/99-culmination-audit-2026-11-14.md](docs/99-culmination-audit-2026-11-14.md) | **Final accounting**: DONE / NOT DONE / AT RISK + preservation manifest + rebuild recipe |

## Estate repos (roles, one line each)

| Repo | Role |
|---|---|
| `prx0r/openpatala` | **Identity** — Work/Edition/Witness/EText, API `:8821`, MCP 8 tools |
| `prx0r/trika-x` | **Proof + verification** — Lean formal-trika, traces, federation gateway |
| `prx0r/translation-work` | **Evidence** — canonical translation layers T1→L4, Scholar pipeline |
| `prx0r/svread` | **Surface** — reader site svatantrya.net, Scholar evidence, MCP gateway (live) |
| `prx0r/nibbanahelp` | **Personal** — diary, tensions, relay; journey (owner-gated) |
| `prx0r/bookfactory` · `prx0r/videofactory` | **Render** — gated books / videos (nothing ships ungated) |
| `prx0r/ipvv` | **Source labour** — IPVV translation from scratch, pushing corpus |
| `prx0r/sanskritbench` | **Calibration** — gold sets, proof gates, metric thresholds |
| `prx0r/aoc` | Separate product line (TikTok factory; not Trika chain) |

## Laws (never violated)

- **Machine proposes, human disposes.** No auto-sign, no auto-publish, ever.
- **Tiers on every claim** (T/R/E/C/H/X). A reconstruction never promotes itself.
- **Fail-closed.** Timeouts, blocks, empty responses are ERRORS, never passes.
- **BLOCKED ≠ PASS.** A blocked gate is reported with its reason.
- **Private stays private.** Diary material ships only with explicit, scoped, revocable consent.

## Status

V1 engineering is complete and live (see [live state](docs/60-live-state.md)).
What remains: owner switches (OAuth, indexing, Zenodo, witnesses, rotation) and
scholarly coverage climb. See the [V1 tracker](docs/70-v1-tracker.md).
