# AGENT RECIPES — tested sequences, with what each actually proves

*Status: CANONICAL. Sixteen recipes an external agent runs against the public
surface (no key, no box). Every one is executable, was run live on 2026-11-14
(`data/recipes-report.json`, 16/16), and every check has a named negative control
(`tools/recipes_run.py --selftest` proves each judge rejects deliberate
corruption). Run them: `python3 tools/recipes_run.py`.*

Each recipe is split into **gather** (live calls → observed) and **judge**
(named checks). A failure names the exact check that broke, not "failed".

---

## R1 — Identity: resolve, never invent

**Calls:** `openpatala__resolve {"q":"bodhapancadasika"}` · `{"q":"zzzz-not-a-work-qqq"}`
**Passes when:** known → `EXACT` with a non-empty `entity.id`; unknown → `NONE`; the known call carried no error.
**What it proves:** the resolver distinguishes an exact hit from a miss and does not fabricate an entity for garbage.
**Why relevant:** an agent must get a stable `work_id` before any downstream call; guessing an id poisons every later claim.
**Negative controls:** status→NONE, id→"", unknown→EXACT, error injected — each must fail.

## R2 — Evidence: layers with verifiable hashes and honest review state

**Call:** `scholar__passage_evidence {"work":"bodhapancadasika","target":"bod-p01-v01"}`
**Passes when:** ≥1 layer, ≥1 `layer_sha256`, every hash is 64-hex, `review_state.default` ∈ {`UNREVIEWED`,`SELF_ATTESTED`}.
**What it proves:** the evidence payload is hash-bearing and its review state is honest by default.
**Why relevant:** an agent quoting a passage must hand the reader a hash and the *real* review state, never a claim of review.

## R3 — Proof: named Lean theorems + a coverage denominator

**Calls:** `formal__trace {"work":"tantrasara-a08","target":"tsa08-p03"}` · `formal__gaps {}`
**Passes when:** verdict `COMPLETE`; ≥1 theorem; every theorem is named (`File :: thm`); gaps carry a `total`.
**What it proves:** the formal chain resolves to named, registered Lean theorems, and coverage carries its denominator.
**Why relevant:** "we checked it" vs "trust us" — an agent must be able to show the theorem names.
**Scope caveat:** `COMPLETE` means *links present*, not "correct or reviewed". Read `verdict_scope`.

## R4 — Coverage honesty: a fraction, never a headline

**Call:** `formal__gaps {}`
**Passes when:** `coverage` is a `n/m` string; `total` a positive int; ≥1 gap listed; `gap_count` equals the list length — or, if the server truncates, `truncated:true` and `returned == len(gaps)`.
**What it proves:** coverage is never a bare number; the gap list is consistent with `gap_count`.
**Why relevant:** the whole estate's honesty rests on never quoting coverage without its gap list. *(This recipe found a real bug: the server returned `gap_count:138` with only 60 gaps and no truncation flag. Fixed in trika-x: full list returned + explicit `returned`/`truncated`.)*

## R5 — Outsider verification (the killer recipe)

**Calls:** `GET /data/verify/bodhapancadasika-bod-p01/manifest.json` → `GET .../source.txt` (+ a `layer-*` artifact)
**Passes when:** manifest 200; source artifact 200 and non-empty; recorded sha is 64-hex; **recomputed sha256 equals the recorded hash**; a layer artifact also verifies if present.
**What it proves:** an outsider recomputes the published bytes' sha256 with no code and no account and it matches.
**Why relevant:** this is the answer to "how do I know this is real?" — fetch, `sha256sum`, compare. If this fails, nothing else is citable.

## R6 — Full research flow (identity → evidence → proof)

**Calls:** `resolve {"q":"paramarthasara"}` · `passage_evidence {"work":"paramarthasara","target":"param-p04-v29"}` · `formal__trace {"work":"paramarthasara","target":"param-p04"}`
**Passes when:** identity `EXACT`, `work_id=="paramarthasara"`; evidence has layers; trace `COMPLETE`; trace `identity` hop `BOUND`.
**What it proves:** one work carries the whole chain end to end and the trace's identity hop binds to the resolved work.
**Why relevant:** this is the actual task — resolve, read, prove, with identity consistent across all three. Read at verse scope, prove at chunk scope.

## R7 — Fail-closed: nothing fakes success

**Calls:** unknown tool · `passage_evidence` bad target (`../etc`) · `resolve {"q":""}`
**Passes when:** unknown tool errors; bad target errors; empty query returns `NONE`/`INVALID_QUERY`.
**What it proves:** the surface fails closed — bad input errors, empty input resolves to nothing, never a silent empty success.
**Why relevant:** an agent must trust that an empty answer means "no result", not "the tool quietly did nothing".

## R8 — Honest boundary: proof ≠ readable evidence

**Calls:** `passage_evidence {"work":"tantrasara-a08","target":"tsa08-p03"}` · `formal__trace` same
**Passes when:** evidence is *present* **or** explicitly *withheld* (never a silent empty), and the trace returns a real verdict (`COMPLETE`/`PARTIAL`).
**What it proves:** a proof-complete chunk may still withhold its reading, and the surface says which.
**Why relevant:** prevents an agent from assuming "proof exists ⇒ passage readable" and inventing a reading where none is served. *(Real example: `tantrasara-a08/tsa08-p03` — trace COMPLETE, reading withheld.)*

## R9 — Bibliography search: find a work by name/alias/identifier

**Call:** `openpatala__search_bibliography {"q":"tantra","limit":3}`
**Passes when:** status `OK`; `total` a positive int; ≥1 result; `response_sha256` 64-hex; first result carries a `work_id`.
**What it proves:** bibliographic search is real (ranked works + a stable response hash), not a title-keyword guess.
**Why relevant:** finding a work is the first half of every research task; the response hash lets a caller cite the exact answer.

## R10 — Treeka: the argument graph

**Call:** `treeka__chain {"work":"tantrasara-a08"}`
**Passes when:** `rows ≥ 1`; entries present; every entry names `work` + `verses`.
**What it proves:** the work→passages argument graph is assembled and every entry is anchored to a verse range.
**Why relevant:** an agent exploring a text needs the passage graph, not isolated chunks; this proves the join exists and is anchored.

## R11 — Learning: a real, gate-bearing level

**Call:** `scholar__wheel_level {"level":1}`
**Passes when:** level echoes 1; title present; a server-scored `gate` object present; prompt substantive (>100 chars); a source `url` present.
**What it proves:** the learning surface serves a real level (prompt + scoring rule + source), not a bare form list.
**Why relevant:** teaching Sanskrit needs the level text AND the server-side gate so a score is never self-reported.

## R12 — Translation state: gold vs machine-proposed

**Call:** `translate__status {"work":"tantrasara-a08"}`
**Passes when:** registry work matches; `STATUS` present; registry reports a verse count.
**What it proves:** the translation lane's public read returns the work's registry state honestly (the payload distinguishes gold from machine-proposed).
**Why relevant:** an agent must say whether a work is gold or merely machine-proposed before quoting it.

## R13 — Evidence rows: a theorem's grounds

**Call:** `formal__evidence {"theorem":"Kancuka.lean :: count_5"}`
**Passes when:** found; a `kind`; cites ≥1 chunk; the chunk carries a `locator`, a `tier` (T/R/E/C/H/X), a `status`; the `note` says registry refs are **not entailments**.
**What it proves:** the theorem's registry row is exposed with its tier and the passages it is bound to.
**Why relevant:** this is how "Sanskrit is being proved" becomes auditable — the theorem names its passages, and the payload refuses to claim entailment.

## R14 — Harness receipts: proof leaves a receipt

**Call:** `formal__runs {}`
**Passes when:** runs ≥1; latest has a timestamp; control + recognition exit 0; Lean version recorded.
**What it proves:** each rung has a recorded run (Lean version, exit codes, rev), not just a claim of passing.
**Why relevant:** a proof without a receipt is theatre.

## R15 — Axiom hygiene: no smuggled 'proof'

**Call:** `formal__axioms {}`
**Passes when:** exit 0; static report says CLEAN; forbidden markers (`sorry`, custom axiom, `native_decide`) were scanned.
**What it proves:** the Lean corpus carries no placeholders/axioms (static half; kernel verdict needs pinned Lean).
**Why relevant:** stops "proved" from meaning "assumed".

## R16 — Provenance chain: one bundle, Sanskrit → proof

**Call:** `formal__trace {"work":"tantrasara-a08","target":"tsa08-p03"}`
**Passes when:** verdict COMPLETE; source `bytes_sha256` is 64-hex; layers present; formal status recorded (`REGISTERED`/`none`); identity hop `BOUND`/`UNRESOLVED`.
**What it proves:** the whole audit chain lives in one hash-pinned bundle: source bytes → layers → formal status → identity.
**Why relevant:** this is the object an essay or DOI cites — one bundle from Sanskrit bytes to proof and identity.

See `docs/formal-audit-chain.md` for how these hops compose into the proven method.

---

## The pattern behind all sixteen

**resolve identity → read evidence (hashes + review state) → check proof →
report gaps → verify bytes.** Every step answers honestly: `NONE`, `UNREVIEWED`,
`WITHHELD`, `PARTIAL`, `UNPINNED` are valid answers and must be reported as such.

## How the tests are themselves tested

`tools/recipes_run.py --selftest` runs each recipe live (must pass) and then
applies deliberate corruptions to the observed data (e.g. `verdict→PARTIAL`,
`recomputed_matches→false`, `evidence_is_honest→false`) and asserts the judge
**fails** on every one. A recipe that cannot be made to fail is not a test.
Current: all 16 pass live, every mutation caught.
