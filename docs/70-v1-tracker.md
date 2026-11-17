# 70 — V1 tracker (definition of done + repair queue)
*Status: CANONICAL. V1 definition of done, repair queue, owner switches. (2026-11-14.)*

*The single progress ledger. V1 is engineering-complete and live; what remains
is owner switches plus scholarly coverage. No feature creep.*

## V1 definition of done

### Live surfaces
- [x] Reader + Sanskrit + practice + bibliography + Scholar + plugins pages load
- [x] Same-origin embeds work (wheels + data/sanskrit) — fixed, deployed, tested
- [x] Public MCP bundle live (`mcp.svatantrya.net`, 51 tools, no key)
- [x] Owner console live (`mcp.sanskrit.help`, 210 tools, bearer)
- [x] Formal/Lean tools public (`formal.svatantrya.net`): `formal__trace` → COMPLETE
- [x] Public instructions speak plain layer names + "machine-checked"
- [x] ChatGPT acceptance suite T0–T15 passes live 16/16 (trika-x: suite + runner + CI wrapper; PR open)
- [x] GEO files live: robots.txt allows AI crawlers + names sitemap; 1963-URL sitemap exposes 906 claim pages; claim JSON-LD carries honesty states (BLOCKED/UNPINNED/UNBOUND/UNREVIEWED); llms.txt served
- [x] **Per-layer sha256 + review state in `scholar__passage_evidence`** — live 2026-11-16 (R2: 7 layers, 7 sha, `UNREVIEWED`)
- [x] `llms.txt` points agents at live MCP endpoints (public + console URLs live 2026-11-16)
- [ ] **Google indexing confirmed** (owner: Search Console — no submission portal exists for organic AI citations; crawlable surface is the whole lever)

### Identity (OpenPāṭala)
- [x] check.py GREEN + 2 recorded BLOCKED — honest
- [x] Live counts documented with provenance (1034 = 555 + 479 shells)
- [x] Source-aware bibliography search live (q-path crash fixed)
- [ ] Chunk↔verse remainder (translation-work lane)
- [ ] Witnesses 0 (needs manuscript eyes — V1 accepts UNPINNED)

### Formal spine
- [x] Lean control 53/0, recognition 26/0
- [x] EVIDENCE 206/155/0, table rc=0, axiom CLEAN, freshness SHARP
- [x] 909 traces (236 COMPLETE / 673 PARTIAL)
- [x] Treeka chain/frontier live; gap report queryable
- [x] Coverage 16/154 published with gap list (climbs by scholarly rungs)

### Hygiene / safety
- [x] Catalog SHARP (115), pretest GREEN, suite 107 OK, bridge E2E 8/8
- [ ] **Rotate the pasted bearer + GitHub token** (owner, SECURITY)
- [ ] Disk reclaim ≥15% (owner eyes on 6G+ trees)
- [ ] Nightly verify 7 green days confirmed (owner)

## Repair queue (ordered, no creep)

1. **[agent — DONE 2026-11-16]** `scholar__passage_evidence`: per-layer sha256 + review state live (R2 PASS).
2. **[agent — DONE 2026-11-16]** `llms.txt`: live MCP endpoint URLs present (public + console).
2. **[owner]** Revoke the leaked GitHub token + MCP bearer; reconnect write app.
3. **[owner]** Search Console + sitemap submit; confirm indexing.
4. **[owner]** Credentials rotation; disk reclaim; nightly-green confirmation.
5. **[agent]** Close/merge remaining open PRs (trika-x #15 trace refresh).
6. **[owner]** OAuth → directory submission (the public finish).

## Owner switches (the real finish)

- [ ] OAuth (per-user) → public writes + directory submission
- [ ] Practice session token → `progress__*`
- [ ] Plugin directory submission (index/sanskrit/practice/formal/translate)
- [ ] Zenodo token → first DOI
- [ ] Witness verification (NGMPP)
- [ ] Token rotation

## Recipe family scope

R1 pipeline exists (compile → check → pushback); consent stays owner-gated.
R2–R8 are specs; R9 explicitly NOT YET. V1 ships the spine + surfaces, not the
media factory. If V1 must include one recipe end-to-end, the cheapest honest
one is R1 with a scoped consent — an owner decision, not more code.
