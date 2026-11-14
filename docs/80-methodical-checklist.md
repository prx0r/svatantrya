# Methodical checklist — estate verification, one step at a time (started 2026-11-14)
*Status: CANONICAL. Methodical verification, one step at a time. (2026-11-14.)*

*Rule: no step is marked done without the command that proved it and the
output observed. A step that fails stops the checklist — fix, re-run, record.
Nothing here is remembered; everything is reproduced.*

## Step 1 — trika-x: what it is, is it working, how do agents use it ✅ DONE

### 1a. What trika-x is

`prx0r/trika-x` is the estate's **proof + verification** repo: Lean
formalizations of Trika doctrine (`formal-trika/control/`,
`/recognition/`, `/buddhist/`, `/frontier/`), the machine-checked evidence
registry (`EVIDENCE.json`), the 909-bundle trace compiler, the treeka gap
report, and the MCP federation gateway everything else plugs into. On box:
`/root/trika-x`, branch `main` @ `d01f65d`, tree clean. Two PRs open and
explicitly **not** blocking this step: #19 (D-DSP pilot, awaiting assessor),
#15 (other agent's trace refresh).

### 1b. Is it working — verification battery (all run live this session)

| Gate | Result | Command |
|---|---|---|
| EVIDENCE registry | **206 theorems · 155 entries · 2 exemptions · 1 generated · 0 problems** | `python3 formal-trika/tools/evidence_check.py` |
| TABLE readings | **rc=0** | `python3 formal-trika/tools/table.py --check` |
| Axiom audit | **CLEAN (static)** | `python3 formal-trika/tools/axiom_audit.py --check` |
| MCP catalog | **SHARP, 115 tools / 8 families** | `python3 tools/mcp_catalog.py --check` |
| Federation pretest | **GREEN (28 expected tools)** | `python3 tools/federation_pretest.py` |
| Essay derivation | **6 essays, 0 BROKEN** (all PARTIAL, honestly) | `python3 formal-trika/tools/essay_derive.py` |
| Lean control | **53 PASS / 0 FAIL** (positives + must-fail twins) | `sh formal-trika/control/run.sh` (Lean 4.34.1) |
| Lean recognition | **26 passed / 0 failed** | `sh formal-trika/recognition/run.sh` |
| Full suite | **107 tests OK** | `python3 -m unittest discover -s formal-trika/tests` |
| Freshness | **SHARP on clean main checkout** | `python3 formal-trika/tools/freshness.py --check` |

**Anomaly found and resolved, not hidden:** the first freshness run reported
DRIFT (manifest 11109 → 11108). Root cause: this box's `/root/svread`
checkout was sitting on the unmerged private-relay patch branch, whose
manifest legitimately lists one fewer asset (nibbana removed). Re-ran against
a clean `origin/main` worktree → **SHARP**. The gate is fine; the checkout
was dirty. Failing checkouts, not failing gates — record the difference.

**Verdict: trika-x works.** Every gate the repo defines passes on main as of
2026-11-14.

### 1c. How ChatGPT uses it — proven end-to-end over the public MCP

ChatGPT connects to `https://mcp.svatantrya.net/mcp` (Streamable HTTP,
`MCP-Protocol-Version: 2025-06-18`, no auth on reads). Reproduced exactly
what a connector does, with raw calls, this session:

1. **Handshake**: `POST /mcp` `{"method":"initialize"}` → `protocolVersion`
   `2025-06-18`, server instructions naming the read sheaf. ✅
2. **Discovery**: `tools/list` → **51 tools**: openpatala 8, scholar 17,
   federation 1 (guide), **formal 7**, treeka 2, translate 6, compose 10. ✅
3. **Proof**: `tools/call formal__trace {work: tantrasara-a08, target:
   tsa08-p03}` → verdict **COMPLETE**, **9 REGISTERED Lean theorem rows**
   (first: `AnswerKey.lean :: key_five_kancukas`). ✅
4. **Evidence**: `tools/call scholar__passage_evidence {work:
   bodhapancadasika, target: bod-p01-v01}` → 9,474 bytes, Sanskrit + layers +
   `projection_sha256`. ✅
5. **Refusal**: write-sheaf tools without a bearer → `-32001 unauthorized`
   (OAuth not issued; the bridge says so instead of faking acceptance). ✅
   (verified on the trika-x bridge selftest this session; public hosts 401
   on bearer routes — spot-checked `studio` → 401.)

**Verdict: the ChatGPT path serves real trika-x proofs today.** A connector
pointing at the public bundle gets machine-checked theorems with receipts,
not marketing copy.

### 1d. How any other agent uses it (Google-agent angle) — proven at SDK level

"Google agent" here means: any agent framework that speaks MCP (Google ADK
`MCPToolset`, Claude, open agents) — no Google-specific endpoint exists or is
needed. Proven with an **independent client stack** (FastMCP SDK `Client`,
not curl) against a **different host** (`formal.svatantrya.net`):

- `list_tools()` → **10 tools**: guide + 7 formal + 2 treeka. ✅
- `call_tool('formal__gaps', {work: 'vbt'})` → 301-byte gap report. ✅

Two independent stacks (raw JSON-RPC + SDK client) × two independent hosts
(public bundle + formal host) = the surface is protocol-standard MCP, not a
single demo path. Any MCP-compatible agent consumes it identically. Auth story
for agents: public reads need no credential; bearer hosts answer 401 without
one; writes require OAuth that does not exist yet (fail-closed, stated).

### Step 1 verdict

**trika-x is real, green, and reachable by agents today** — proven by its own
gates (53+26 Lean, 107 tests, SHARP ledger) and by two live agent paths
returning real theorems. The one anomaly found (freshness DRIFT) was traced
to a dirty checkout, re-proven SHARP on clean main, and recorded rather than
smoothed over.

---

## Queued (unplanned — defined when we get there, not before)

- Step 2: _TBD by owner_
- Step 3: _TBD by owner_

*One step at a time. No step is real because a file exists — only because a
fresh run says so.*
