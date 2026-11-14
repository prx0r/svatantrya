# atlas + corpus — patalacheckpoints, tantrasara, aoc
*Status: REFERENCE. Per-repo reference: role, gate, honest state. (2026-11-14.)*

## patalacheckpoints — ATLAS + prior art

**Role:** the canonical bibliography and source-resolver design ("essays.
tantrafiles.xyz — the Śaiva Tantra Atlas"). It is the **bibliography source of
truth** the estate references rather than forks: `atlas/audited.ts` (depth) +
`atlas-bibliography.json` (index) feed the box DB via trika-x
`seed_atlas_biblio.py`.

**Honest state:** its bibliography is the reference; its **Lean claims are
NONE** (do not treat any formal claim here as proof). Atlas tip is dormant
(Oct 7); the live lanes carry the work. Gate: repo-local.

## tantrasara — WORKED EXAMPLE

**Role:** Tantrasāra (Abhinavagupta) → six-section argument + essay-0 + rungs —
a worked instance of the same machine (structure → translation → argument →
formal → essay). Reference for how a single text runs the full chain.

**State:** example corpus; not a separate platform. Gate: repo-local.

## aoc — SEPARATE PRODUCT LINE

**Role:** the TikTok slideshow factory for AI Onboard (plus POW companions).
**Explicitly not part of the Trika chain** — a separate business track. Listed
here so agents don't mistake it for a Trika dependency.

**State:** 13 trade segments, 11 templates, 88 claims, 75 tests green; gated,
receipted. Gate: `python3 -m pytest tests/ -q`.

## Why these are grouped

These three are **inputs and neighbours**, not pillars of the identity→proof→
surface chain:
- patalacheckpoints supplies bibliography (reference, not fork).
- tantrasara is a worked example of the machine.
- aoc is a separate business, documented so it is not confused with Trika work.
