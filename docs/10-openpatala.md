# 10 — OpenPāṭala (identity root)
*Status: CANONICAL. Identity root: what works, counts, gate. (2026-11-14.)*

> "OpenPāṭala is not the archive. It is the memory and research protocol over
> the archives."

OpenPāṭala answers one question: **which work/edition/passage is this?** It does
not translate, render, or publish. Everything downstream (traces, essays,
factories, ChatGPT tools) cites it as the root.

## Live state (verified 2026-11-14, `check.py --status` → GREEN)

| Table | Rows | Note |
|---|---|---|
| works | **1034** | 555 enriched + 479 Muktabodha identity shells |
| passages | 909 | = translation-work ledger total |
| editions | 581 | 102 enriched + 479 Muktabodha |
| etexts | 566 | sha-pinned; bytes on disk/R2, never blobs in DB |
| assertions | 1559 | unchanged by the Muktabodha ingest |
| translations | 121 | 16 atlas + 5 Tantraloka biblio + 101 ours |
| people | 20 | 12 atlas + 8 |
| witnesses | **0** | UNPINNED box-wide (manuscript eyes outstanding) |

**Provenance of the growth:** 555→1034 is one scripted Muktabodha load at
2026-11-11 10:48:16Z (479 `mukta-M#####` works, provider `PT_PROVIDER_muktabodha`,
0 assertions/translations, rights NULL). The 555 enriched works are untouched.
See trika-x `docs/log/DB-PROVENANCE-2026-11-14.md`. Shells carry no rights, so
they are **not publishable** until rights are set — identity only, never content.

## Gate

```sh
cd /root/openpatala && python3 check.py --status
# GREEN + 2 recorded BLOCKED: adapters discover nothing (upstream gap);
# witnesses 0 (structural). BLOCKED is never PASS.
```

## API (box, `:8821`)

`GET /health`, `/v1/works`, `/v1/works/{id}`, `/v1/bundle/{id}`.

```sh
PYTHONPATH=. nohup python3 -m uvicorn patala.api:app --port 8821 --host 127.0.0.1 &
```

## MCP (8 tools, live)

`patala/mcp_server.py` (stdio): `resolve`, `get_bundle`, `search`,
`search_bibliography` (arg is `q`), `bibliography_facets`,
`get_bibliography_dossier` (arg is `work_id`), `get_frontier`, `get_health`.

The `q` full-text path was crashing on unescaped SQL `LIKE` literals
(`%TITLE%`); fixed 2026-11-14 (`%%TITLE%%`), re-smoked against the live box
(158 results for "tantra"). Bound filter params were already correct.

## Rules of this layer

- Identity is not philological truth: a work ID plus a shared GRETIL string is
  a **candidate** mapping, never a proven edition.
- UNRESOLVED / CANDIDATE / UNPINNED are valid states, never silently promoted.
- Missing/UNRESOLVED = draft-only downstream (no ship, sell, post, publish).
- Nothing is "real" because a file exists: a claim needs a logged, reproducible gate.
