# 40 — Federation + MCP (one agent entry point, ChatGPT plugins)
*Status: CANONICAL. One MCP surface: topology, live endpoints, read sheaf. (2026-11-14.)*

One agent entry point. OpenPāṭala is the identity root; every other system is a
child MCP. The parent multiplexes, prefixes, routes FailOpen, and serves
identity + a navigation guide itself. **Nothing here auto-signs, auto-publishes,
auto-ships, or grants rights.**

## The gateway (trika-x reference parent)

```
Agent (1 MCP connection, stdio NDJSON: initialize / tools/list / tools/call)
  ▼
federation_gateway.py
  │  tools/list → local tools + <child>__<tool> per live child
  │  tools/call → route by first segment; Unknown tool on miss;
  │               FailOpen (dead child excluded, never fatal)
  ├─ openpatala__resolve / openpatala__coverage   (local, source-map backed)
  ├─ federation__guide                            (local, navigation map)
  ├─ scholar__*        svread Scholar (41 tools: evidence, wheels, certificates, essays, reviews)
  ├─ bookfactory__*    bookfactory bf_mcp (22 tools, draft-only + gated builds)
  ├─ translation__*    translation-work shastra (16 tools, no push/signoff ever)
  ├─ video__*          videofactory vf_* (18 tools, gated renders; ship defaults False)
  └─ formal__*         trika-x formal-trika read-only tools (7: trace/bridge/evidence/table/gaps/runs/axioms)
```

Live: **115 tools / 8 families** (catalog SHARP; pretest GREEN). The
`federation__guide` speaks verification-first: formal chain before reading, and
layers in plain words (draft-translation → song), machine keys still accepted.

## The live public surface (measured 2026-11-14)

| Endpoint | Auth | What |
|---|---|---|
| `https://mcp.sanskrit.help/mcp` | bearer (owner console) | **210 tools / 7 servers** — 13 trees, read + write |
| `https://mcp.svatantrya.net/mcp` | none | **51 tools**: openpatala + scholar reads + formal |
| `https://sanskrit.svatantrya.net/mcp` | none | 12 scholar reads, plain-words layer names in instructions |
| `https://practice.svatantrya.net/mcp` | reads open, writes bearer | 5 wheel reads + 3 scored |
| `https://formal.svatantrya.net/mcp` | none | 10 tools: guide + 7 formal + 2 treeka |
| `https://index.svatantrya.net/mcp` | none | 5 openpatala reads |
| `https://translate.svatantrya.net/mcp` | none | 6 shastra teaching reads |
| `studio / factory / essay / books / video / tutor / nibbana .svatantrya.net` | bearer (owner) | drills, books, video, sessions, relay |

Proven from the internet, no auth: `formal__trace tantrasara-a08/tsa08-p03` →
verdict **COMPLETE**, 9 Lean theorem rows. `tools/list` on the public bundle →
51 tools including `openpatala__resolve`, `scholar__layers_index`,
`scholar__translation_forks`, `scholar__passage_layers`, `formal__trace`.

## Read sheaf (public without auth)

Layers in plain words, openpatala resolve/coverage/bundle/search, passage
evidence, formal evidence/bridge/table/gaps/runs/axioms, wheels
(harness/level/lookup/verify/certificate), layers index, passage layers,
translation forks, guide. Writes answer `-32001 unauthorized` — OAuth for the
write sheaf is not issued yet, and the bridge says so instead of faking
acceptance.

## Operational facts

- All hosts are systemd units (`svatantrya-mcp*`), `Restart=always`, behind one
  named Cloudflare tunnel; 127.0.0.1-bound servers, one bridge per host config.
- Adding a tool to a FastMCP child is one decorated function; children are
  spawned per call so the gateway picks it up immediately, no redeploy.
- Limits: 60 s/call, 10 concurrent, 64 KB body. Long jobs return `job_id`.
- Monitoring: hourly `/health`; daily `gateway__problems`; compare `tools/list`
  count to the generated `TOOLS.md` catalogue.
- Caveats: one shared bearer (rotate before sharing; treat as root-adjacent).
  No OAuth yet. `workspace` tools can edit repos but never push.
