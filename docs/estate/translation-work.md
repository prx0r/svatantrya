# translation-work — the evidence pillar
*Status: REFERENCE. Per-repo reference: role, gate, honest state. (2026-11-14.)*

## Role

The canonical Sanskrit translation stack. It produces the **layers** every
downstream claim cites: `T1` draft-translation → `L0` literal-gloss (meaning-
forks live here) → `ARGMAP` argument-map → `L2` reading-translation → `C1`
essence → `C2` register-render → `L3` final-translation → `L4` song, per chunk,
each sha-pinned.

It is **evidence, not proof**: trika-x reads its bytes and proves structural
facts about them; svread renders them; nothing here claims a human sign-off.

## Where the data lives

- Per work: `<work>/passages.jsonl` (ledger, locators like `tsa08-p03`),
  `data/<song>.<layer>.json`, `proof/`, `STATUS.json`.
- `REGISTRY.json` — the work registry (gold/partial/pending).
- Layers are additive and versioned; a changed byte invalidates downstream
  approval (recorded, never auto-healed).

## Gate

```sh
cd /root/translation-work && python3 check.py     # their lane's gate
```
Recorded 2026-11-07: canonical 0 failures; 95 works gold in REGISTRY.json.

## MCP

`mcp_server.py` (FastMCP, stdio/HTTP, 34-tool surface as of 2026-11-14):
status, gates, validate, concepts, lore, bibliography, priority, swarm_*.
Read tools are public; writes are owner-gated (safety patch PR #22 proposes a
fail-closed write gate + removal of MCP proof/PASS/push paths — **not merged**;
the live guard is whatever the burn loop owner deploys).

## The hot-loop caveat (important for agents)

`burn/muktabodha` runs an autonomous loop (`ralph` passes every few minutes).
Consequences:
- Any trace/excerpt compiled against it **decays within minutes** — freeze →
  refresh → merge, never refresh against a moving target.
- My safety PR #22 targets the burn head and conflicts as the loop advances;
  it is an artifact for the burn owner to rebase at merge time.
- Do not assume a "pending/claimed" queue count is stable; read it live.

## Ownership boundary

trika-x and svread read this repo; they never write it. Layer decisions,
promotion, and the queue belong to the translation-work lane.
