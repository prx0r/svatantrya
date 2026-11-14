# bookfactory + videofactory — the render pillars
*Status: REFERENCE. Per-repo reference: role, gate, honest state. (2026-11-14.)*

## bookfactory — PRINT

**Role:** gated paperbacks, quote cards, and book specs built from compiled
claims. A book is a **thesis with a spine** (see `BOOKS.md`); every entry
cites a source. It ships **nothing ungated** — the gate is fail-closed by
design and all lanes are BLOCKED until a human sign-off path exists.

**Key docs:** `BOOKS.md` (canonical: how a book is defined/built/shipped),
`FACTORY-SPEC.md`, `AGENTS.md`. Gate: `python3 check.py`.
**Honest state:** no production book shipped; the ship path is deliberately
absent until rights + sign-off are wired.

## videofactory — VIDEO

**Role:** a parity render rig; video projects and gated renders. Renders are
gated; `vf_publish` is owner-only and refused over remote MCP (publication is
a separate human step).

**Key docs:** `FACTORY-SPEC.md`, `BARS.md` (quality bars), `docs/MCP.md`.
Gate: `python3 check.py`. **Honest state:** build-only; no production render;
PR #3 (MCP server) and #2 (ChatGPT handover) open.

**Auth work (2026-11-14):** `core/http_auth.py` + tests banked on a branch
(PR #4) — read allowlist public, writes need a bearer, `vf_publish` always
refused remotely. Note: the server has no HTTP layer to hook yet (stdio-only),
so the middleware wiring waits on whichever PR establishes the HTTP surface.

## Auth patches (both factories, from the handoff)

bookfactory has a bearer-gated HTTP adapter (PR #4: read/write token split,
fail-closed unknown tools, 9 tests). Both need a **live FastMCP/Uvicorn
integration check** in the deployment environment before exposing writes —
unit tests use a stdlib shim, not the real runtime.

## The rule for both

Factories **render; they never source.** A pack may only cite locators that
resolve (via openpatala identity + trika-x evidence). A render without
`evidence_refs` is a failed render — that carry-through is an open lane ask
(trika-x backs it; the factories implement it).
