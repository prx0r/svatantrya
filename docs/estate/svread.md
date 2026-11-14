# svread — the surface pillar
*Status: REFERENCE. Per-repo reference: role, gate, honest state. (2026-11-14.)*

## Role

The public reading and verification surface: the site at
**https://svatantrya.net**. It renders the reader, Sanskrit lessons, practice
wheels, bibliography, claim pages, and the Scholar evidence view — all reading
only from gated outputs. It also hosts the **public MCP gateway**
(`mcp.svatantrya.net`) and the owner console (`mcp.sanskrit.help`).

## Live (verified 2026-11-14)

| Surface | URL | State |
|---|---|---|
| Site | https://svatantrya.net | 200 |
| Public MCP bundle | https://mcp.svatantrya.net/mcp | live, ~51 tools, no auth |
| Owner console | https://mcp.sanskrit.help/mcp | live, ~210 tools, bearer |
| Formal host | https://formal.svatantrya.net/mcp | live, 10 tools, no auth |
| Claim pages | https://svatantrya.net/claim/<work>/<target>/ | live, JSON-LD honesty states |
| llms.txt / sitemap | /llms.txt · /sitemap.xml | live; llms names the MCP endpoints |

## Gate

```sh
cd /root/svread && node --test tests/*.cjs                       # reader suite
python3 -m unittest discover -s mcp -p "test_*.py"               # MCP suite
python3 tools/emit_verify.py --check                             # publish gate (fail-closed)
python3 scripts/release_manifest.py                              # asset hashes
```

Deploy is **manual**: `./deploy.sh` (stages a public tree, regenerates the
manifest, `wrangler pages deploy`). Editing files on main does not change the
live site until a deploy runs.

## What svread guarantees

`emit_verify.py` publishes the exact bytes a trace hashes and **refuses on any
mismatch** — nothing reaches a reader without passing it. Claim pages carry
machine-readable honesty states (`deterministic_gate: BLOCKED`,
`witness: UNPINNED`, `review: UNREVIEWED`, `publication: NOT_AUTHORIZED`).

## Recent repairs (2026-11-14, merged)

- Same-origin iframe embeds unblocked (`/wheels.html`, `/data/sanskrit/*` →
  `SAMEORIGIN`, everything else `DENY`).
- `scholar__passage_evidence` now returns **per-layer sha256** + `stack_sha256`
  + `review_state` (default `UNREVIEWED`; signoffs surfaced verbatim).
- `llms.txt` now names every live MCP endpoint (was 0).
- Private nibbana relay removed from the public surface (staged deploys).

## Ownership boundary

svread disposes of its own emitters and deploy. trika-x/openpatala never write
it; they publish *into* it via the documented gates.
