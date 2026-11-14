# ipvv + sanskritbench — source labour and calibration
*Status: REFERENCE. Per-repo reference: role, gate, honest state. (2026-11-14.)*

## ipvv — source labour + pushing corpus

**Role:** Abhinavagupta's Īśvarapratyabhijñāvivṛtivimarśinī translated from
scratch, plus the *pushing* corpus (question → text's answer → sharper
question sessions with verdicts). Live site: **https://ipvv-a8u.pages.dev**
(200). The pushing sessions are conjecture mines — they feed trika-x's crux
queue (read-only export).

**State (honest):** 49 IPVV chunks are `BLOCKED / PROOF_NOT_RUN`; the pushing
INDEX holds ~57 records. This is raw material, not finished translation.

**Gate:** repo-local (`AGENTS.md`); no single `check.py` gate. Treat outputs as
candidate until the lane signs.

**Worker:** `worker/src` (Cloudflare) hosts auth + server-scored wheel gates
(Google site auth, ORCID publishing). PR #12 (wheel gates) is mergeable.

## sanskritbench — calibration, never verdicts

**Role:** gold sets, a proof gate, and `tau` meta-evaluation for translation
quality. **Advisory by design** — a metric that auto-passes alone is a bug.
Foundation done; the tau table is PENDING (CPU calibration only, quota/GPU for
scale). 3×3 smoke run `54b08b41` is the logged reference (null result).

**Gate:** `python3 check.py` (lane). Thresholds are stamped; the gate NEVER
grades a translation as correct on its own.

**Why it matters here:** sanskritbench calibrates the metrics trika-x and
svread display; it never promotes a claim. The three stamps stay separate —
bytes (hashes), mechanics (certificates/Lean), meaning (human sign-off).
