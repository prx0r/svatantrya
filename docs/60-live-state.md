# 60 — Live state (verified 2026-11-14)
*Status: CANONICAL. Verified live endpoints and counts with reproduction commands. (2026-11-14.)*

Every line below was produced by running the command shown, on the box or over
the internet, this session. Re-run any of them; a number that doesn't reproduce
is the highest-severity finding in this project.

## Formal spine

| Check | Result | Command |
|---|---|---|
| Lean control | **53 PASS / 0 FAIL** | `sh formal-trika/control/run.sh` (trika-x, Lean 4.34.1) |
| Lean recognition | **26 passed / 0 failed** | `sh formal-trika/recognition/run.sh` |
| EVIDENCE | **216 theorems · 161 entries · 2 exemptions · 1 generated · 0 problems** | `tools/evidence_check.py` |
| Coverage | **16/154 chunks (10%)** | same |
| TABLE | **rc=0** | `tools/table.py --check` |
| Axioms | **CLEAN (static)** | `tools/axiom_audit.py --check` |
| Freshness | **SHARP** (provenance: Muktabodha ingest 2026-11-11) | `tools/freshness.py --check` |
| Catalog | **SHARP, 115 tools / 8 families** | `tools/mcp_catalog.py --check` |
| Federation pretest | **GREEN (28)** | `tools/federation_pretest.py` |
| Full suite | **132 tests OK (1 skipped)** | `python3 -m unittest discover -s formal-trika/tests` |
| Bridge E2E (HTTP) | **8/8** incl. real evidence + real trace | `tools/bridge_e2e.py` |
| Layer roundtrip | **9/9** codes↔public names | `tools/layer_names.py` |
| Essay gate | **14/14 tests; 6 essays, 0 BROKEN** | `essay_check` + `essay_derive.py` |
| Traces | **909 bundles (236 COMPLETE / 673 PARTIAL)** | `data/traces/index.json` |

## Identity root

`check.py --status` → **GREEN + 2 recorded BLOCKED** (adapters discover nothing;
witnesses 0). Box DB: **1034 works** (555 enriched + 479 Muktabodha shells,
rights NULL) · 909 passages · 1559 assertions.

## Public internet proof (no auth)

```sh
# formal host: full chain, machine-checked, right now
curl -s -X POST https://formal.svatantrya.net/mcp ... \
  -d '{"method":"tools/call","params":{"name":"formal__trace",
        "arguments":{"work":"tantrasara-a08","target":"tsa08-p03"}}}}'
# → verdict COMPLETE, 9 Lean theorem rows

# public bundle: 51 tools, plain layer names in initialize instructions
curl -s -X POST https://mcp.svatantrya.net/mcp ... \
  -d '{"method":"tools/list","params":{}}'
# → openpatala__resolve, scholar__layers_index, scholar__translation_forks, ...

# site: wheels embed allowed, everything else denied
curl -sI https://svatantrya.net/wheels.html   # → SAMEORIGIN
curl -sI https://svatantrya.net/              # → DENY
```

## Estate counts

2,051 works · 268 translated songs · 44 certificates · 210 console tools ·
7 servers · 13 MCP hosts (systemd, named tunnel, reboot-safe).

## Known drifts (recorded, not hidden)

- svread `PRODUCTION.md` §0 still says "bridge/tunnel not built" — **stale**,
  both are live. svread `data/mcp-registry.json` said 198/scholar-38 — refreshed
  to measured values 2026-11-14.
- Muktabodha 479 shells carry **no rights** → not publishable until set.
- Shared bearer exists (`/etc/svatantrya-mcp.env`) — rotate before sharing.
