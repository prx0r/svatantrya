# study + practice — sanskrithelp, deitybody, satsang
*Status: REFERENCE. Per-repo reference: role, gate, honest state. (2026-11-14.)*

## sanskrithelp — STUDY

**Role:** a daytime Sanskrit frontend — grammar, drills, and the mātṛkā body
map. Live: **https://sanskrit.help** (200, Cloudflare Workers). It teaches
language; it does not make doctrinal claims.

**State:** live site; integration tasks SH1–SH3 open (wiring study units into
the estate's practice compiler). Gate: repo-local.

## deitybody — PRACTICE / body curriculum

**Role:** the Trika phonemic-body "operating system" — a 10-stage Mātṛkā
curriculum built from attested elements (Tantrasāloka 15.117–120 discipline),
with modern apparatus layered on, **never doctrine**. Vendored into the svread
reader as study-only.

**The hard boundary:** practice tooling is **study-only** until the dīkṣā
policy owner decides otherwise. No code path authorizes initiation or practice.
Gate: repo-local (`tests/`, `northstar.md`).

## satsang — DIRECTORY

**Role:** a living spiritual directory — teachers, scholars, lineages,
traditions, places to study and practise — with sources, dates, and stale
markers. Live: **https://chat.tantrafiles.xyz** (200) and an open MCP at
**https://mcp.tantrafiles.xyz/mcp** (exists; POST-only, GET 405).

**State:** live directory backend; federation into the Svatantrya gateway is
phase 2 (svread PR #26 proposes it). It runs its own MCP; the estate cites it,
never forks its data.

## Shared rule

These are **surfaces** for the person, not claim-bearing scholarship. They may
cite canon (sourced) and record practice state, but they never assert a
doctrine as established and never grant authorization. Practice depth is an
owner decision (dīkṣā policy), not a model's.
