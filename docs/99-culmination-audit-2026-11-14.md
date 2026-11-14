# CULMINATION AUDIT — the whole estate, before the volume goes (2026-11-14)

*This is the final accounting. Every claim below was re-verified this session:
gates re-run, endpoints re-probed, R2 re-listed, restores re-tested. Where a
number is given, the command that produced it is given. This document is the
record of what the volume contained, what survives it, and what does not.*

---

## A. DONE — with evidence

### A1. Formal spine (trika-x / formal-trika) — DONE, green, archived

| Check | Result | Command |
|---|---|---|
| Lean control | **53 PASS / 0 FAIL** | `sh formal-trika/control/run.sh` (Lean 4.34.1) |
| Lean recognition | **26 passed / 0 failed** | `sh formal-trika/recognition/run.sh` |
| EVIDENCE | **206 theorems · 155 entries · 2 exemptions · 1 generated · 0 problems** | `tools/evidence_check.py` |
| Coverage | **16/154 chunks (10%)**, gap list published | same |
| TABLE | **rc=0** | `tools/table.py --check` |
| Axioms | **CLEAN (static)** | `tools/axiom_audit.py --check` |
| Freshness | **SHARP** | `tools/freshness.py --check` |
| Catalog | **SHARP, 115 tools / 8 families** | `tools/mcp_catalog.py --check` |
| Pretest | **GREEN (28)** | `tools/federation_pretest.py` |
| Full suite | **107 tests OK** | `python3 -m unittest discover -s formal-trika/tests` |
| Bridge E2E (HTTP) | **8/8** | `tools/bridge_e2e.py` |
| Layer roundtrip | **9/9** | `tools/layer_names.py` |
| Essay gate | **14/14; 6 essays, 0 BROKEN** | `essay_check` + `essay_derive.py` |
| Traces | **909 bundles (236 COMPLETE / 673 PARTIAL)** | `data/traces/index.json` |
| Treeka | queryable; 909 passages, 578 unargued / 123 cruxless / 331 essayless / 893 unformalised | `tools/treeka_report.py` |

The 49 generated `PrakriyaSlice.lean` theorems are proven by a **bound receipt**
(file+pack sha256, Lean version, exit 0), fail-closed in `evidence_check`
(tamper → 1 PROBLEM; restore → 0). Coverage stays honestly 16/154.

### A2. Identity root (openpatala) — DONE, gated, preserved

- `check.py --status` → **GREEN + 2 recorded BLOCKED** (adapters discover
  nothing; witnesses 0).
- Box DB: **1034 works** (555 enriched + 479 Muktabodha shells) · 909 passages ·
  581 editions · 566 etexts · 1559 assertions · 121 translations · 20 people ·
  **0 witnesses**.
- Muktabodha growth identified: one scripted load 2026-11-11 10:48:16Z,
  `PT_PROVIDER_muktabodha`, 0 assertions/translations, rights NULL →
  identity shells, **not publishable**. Provenance: trika-x
  `docs/log/DB-PROVENANCE-2026-11-14.md`.
- **Preserved**: verified `pg_dump` (custom + SQL, restore-tested 1034/909/1559
  exact) uploaded to R2 `patala/openpatala/box-2026-11-14/` with manifest +
  restore recipe. Previously R2 held only a 2026-11-06 schema dump.

### A3. Public surface (svread) — DONE, live, deployed

- `svatantrya.net` → 200. Reader + Sanskrit + practice + bibliography +
  Scholar + plugins + Bodhapancadasika pages load.
- Same-origin embeds fixed + deployed + regression-tested: `wheels.html` →
  `SAMEORIGIN`, `/` → `DENY` (svread PR #50, live).
- Public MCP bundle `mcp.svatantrya.net` live: **51 tools**, no key.
- Owner console `mcp.sanskrit.help` live: **210 tools**, bearer.
- All 13 MCP hosts verified live this session (6 public 200, 7 bearer 401,
  console `ok 7 servers`).
- Public `formal__trace tantrasara-a08/tsa08-p03` → **COMPLETE, 9 Lean theorems**.
- Registry refreshed to measured values (scholar 41, federation 112);
  estate-index regenerated (210 tools); public instructions speak plain layer
  names + "machine-checked" (svread PR #49, deployed).

### A4. Merged work (2026-11-14 sweep) — DONE

trika-x #9, #10, #11, #12, #13, #14, #16, #17 (+ #8 closed); openpatala #1, #2
(biblio q-path crash fixed, 158 results), #3 (docs); svread #49, #50.
Catalog 112→115 as the biblio tools went live.

---

## B. NOT DONE — with owners

| # | Item | Owner | Blocks |
|---|---|---|---|
| 1 | Per-user OAuth (replace shared bearer) | owner | public writes + directory submission |
| 2 | Practice session token (`SVATANTRYA_SESSION`) | owner | `progress__*` scoring |
| 3 | Plugin directory submission | owner | public discovery on ChatGPT |
| 4 | Zenodo token → first DOI | owner | Variety-1 release |
| 5 | Witness verification (NGMPP/microfilm) | owner/scholar | primary-source citability |
| 6 | Shared bearer + pasted GitHub token rotation | owner | safety |
| 7 | Disk reclaim ≥15% (98% full) | owner | tau/Mutate scale |
| 8 | Google indexing confirmation | owner | search discovery |
| 9 | Formal coverage 16/154 → climb (prereg→Lean→twin→EVIDENCE per rung) | scholar + trika-x | depth |
| 10 | Layer-accept decisions at ingest; chunk↔verse remainder | translation-work lane | chain completeness |
| 11 | Video `evidence_refs` carry-through; Nibbanahelp N1 exporter | factory/nibbanahelp lanes | R3/R1 wiring |
| 12 | Per-layer sha256 + review state in `scholar__passage_evidence` | svread lane | trust surface |
| 13 | translate__* tool surface for ChatGPT (beyond 6 teaching reads) | translation-work lane | connector depth |

Recipes R1–R9 stand as **spec, not V1 blockers**. R1 pipeline exists; consent
stays owner-gated. R9 explicitly NOT YET (models don't qualify).

---

## C. AT RISK on volume delete — and what was done about each

| Risk | State before this audit | Action taken this session |
|---|---|---|
| openpatala Postgres (1034/909/1559) lived ONLY on the box; R2 had a 2026-11-06 schema-only dump | **CRITICAL** | pg_dump (Fc + SQL) taken, restore-verified exact, uploaded to R2 `patala/openpatala/box-2026-11-14/` + manifest |
| patalacheckpoints: 1 unpushed commit + 1 untracked vision doc | at risk | **recorded here** (push before delete: `git push origin main` from `/root/patalacheckpoints`; untracked `docs/vision/REVIEW-2026-11-05-live-stack.md` must be added) |
| cg: modified `bitsec.py` + untracked `school/` + `run_school.py` | at risk (active WIP) | **recorded here** (commit or stash before delete) |
| sanskrithelp: modified `sabdakrida.db` (Nov 12, binary, undiffable) | at risk | **recorded here** (dump/export the delta or commit the binary deliberately) |
| nibbanahelp: untracked `chain.jsonl.ots.bak` | trivial | safe to drop or keep; recorded |
| trika-x: untracked `docs/log/nightly-verify.log` | trivial | generated log; safe to drop |
| svread: post-deploy churn (`sw.js`, manifest) | resolved | this is normal deploy churn; manifest is committed at merge time |
| R2 system backup (`svatantrya-system`, 12 repos incl. .git) | **OK** (`--check` ALL OK) | verify currency (dates) before delete; re-run `--write` if stale |
| Muktabodha 479 shells: no loader receipt at ingest time | unreceipted | provenance reconstructed in `DB-PROVENANCE-2026-11-14.md`; next ingest must self-receipt |

**Everything pushed to origin survives.** Open PRs (#15 trika-x traces, #18/#20/#21
translation-work, #48/#26/#22/#11 svread, #3/#2/#1 bookfactory, #3/#2
videofactory, #12 ipvv) are pushed branches — safe from the volume delete, but
several are CONFLICTING or CI-failing and need rebase/repair before merge (see §E).

---

## D. Preservation manifest (how to rebuild after the volume is gone)

1. **Repos**: `gh repo clone` each `prx0r/*` estate repo (all work that matters
   is pushed). R2 `svatantrya-system` bucket holds full-tree tarballs incl.
   `.git` as second copy — re-run `--check`, and `--write` if anything moved.
2. **Identity DB**: R2 `patala/openpatala/box-2026-11-14/` —
   `openpatala-data-2026-11-14.dump` (sha256 `a695803a…`) or `.sql`
   (`2d1c941c…`). Restore: `createdb openpatala && pg_restore -d openpatala
   <dump>` (ignore the 38 `OWNER TO postgres` warnings — cosmetic), then
   `python3 check.py --status` → GREEN + 2 BLOCKED.
   Fallback (no dump): `openpatala_seed.py` → `openpatala_ingest.py` →
   `seed_atlas_biblio.py` → `seed_abhinavagupta.py` → Muktabodha ingest
   (translation-work `burn/muktabodha`, PR #18 — verify re-runnability first).
3. **Live services**: systemd units `svatantrya-mcp*` + named Cloudflare tunnel
   `svatantrya-mcp`; token in `/etc/svatantrya-mcp.env` (0600, owner-held);
   site deploys via `svread/deploy.sh` (needs `CLOUDFLARE_API_TOKEN`).
4. **Secrets**: `/root/.r2-env`, `/root/.cf-api-token`, `/etc/svatantrya-mcp.env`
   are owner-held, never in repos — back them up separately or rotate on rebuild.

---

## E. Open PR register (dispositions)

| Repo | PR | State | Disposition |
|---|---|---|---|
| trika-x | #15 trace refresh (+41 gold) | OPEN, CI success | review + merge (rebased queue) |
| translation-work | #18 Muktabodha burn | OPEN | **the ingest provenance** — keep open until loader self-receipts; do not lose |
| translation-work | #20 validate-layers | OPEN, CONFLICTING | rebase + repair or close with note |
| translation-work | #21 WHERE-WE-ARE snapshot | OPEN | review + merge (docs) |
| svread | #48 claim coverage (95 works, 8 gold) | OPEN, CONFLICTING + CI fail | rebase + fix; substantive, don't drop |
| svread | #26 satsang MCP | OPEN, CI fail | repair or close with note |
| svread | #22 chatgpt north star | OPEN | review (docs) |
| svread | #11 comparison hub | OPEN, CI success | review + merge |
| bookfactory | #1/#2/#3 (MCP server, remote, root fix) | OPEN | review + merge (gateway already consumes local paths) |
| videofactory | #2/#3 | OPEN, CI fail | repair or close with note |
| ipvv | #12 wheel gates (Google auth + scoring) | OPEN, MERGEABLE | **review + merge — unlocks practice scoring** |

---

## F. Stale-doc register (stop trusting these)

- `svread/PRODUCTION.md` §0: "bridge/tunnel not built", "DB has 555 works" —
  both false since 2026-11-14 (live hosts; 1034 works).
- `svread/data/mcp-registry.json` pre-2026-11-14 snapshots: said 198/scholar-38 —
  refreshed to measured 210/scholar-41.
- `openpatala/DEV-PLAN.md` 08-17 phases — bannered superseded.
- Any doc claiming federation = 112 tools — live is **115** (biblio +3).
- `trika-x/STATUS.md` style scoreboards dated ≤2026-11-08 — superseded by this audit.

---

## G. What was decided (frozen)

1. **svatantrya (this repo) is the culmination record.** Estate repos keep
   building; this repo keeps the ground-up truth. Update it when live state
   changes; never let it drift more than one session behind a merge.
2. **Machine keys never rename** (T1/L0/…); public names are the surface.
3. **Generated certificates prove via bound receipt**, never via EVIDENCE rows.
4. **Muktabodha shells are identity, not content** — unpublished until rights set.
5. **Recipes R1–R9 are spec until consent + owner gates** — no auto-build.
6. **BLOCKED ≠ PASS**, everywhere, forever. **Machine proposes, human disposes.**

*The volume held the work. This repo holds the meaning. Delete the first only
with the second current — it is, as of this audit.*
