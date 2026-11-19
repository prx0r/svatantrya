# REPORT — svread's philosophy corpus, essays, and what is publishable (2026-11-19)

*Status: AUDIT. Every number below is produced by a command named in this file.
Nothing here is a scholarly verdict; it is an inventory plus a publish path.*

---

## 1. What "the philosophy stuff" actually is

There are four layers, and they are easy to confuse:

| Layer | Where | What it is | State |
|---|---|---|---|
| **Thesis / northstar** | `/root/svatantrya/THESIS.md`, `NORTHSTAR-2026-11-17.md`, `NORTHSTAR-2-2026-11-17.md`, `docs/00-thesis.md` | The owner's programme: what the estate is for, the F1–F10 research tracks, the product target | CANONICAL, owner words in places |
| **Operational plans** | `svread/MASTERPLAN3.md`, `svatantrya/MASTERPLAN4.md`, `svread/ENDGAME*.md`, `svread/endgame/` | Build order, tiers, endgame recipes, per-repo roles | CANONICAL/reference |
| **Machine-checked spine** | `/root/trika-x/formal-trika` | 202 Lean theorems, 202 EVIDENCE entries, 31 works pinned, 910 trace bundles | Machine-checked inside finite models; human review separate |
| **Drafts meant to be read by humans** | `svatantrya/docs/papers/`, `docs/ratie-paper-2026-11-16.md` | Two papers + one historical assembly | DRAFT/HISTORICAL, **no DOI, no peer review** |

So "the original philosophy" is not one document. It is **a thesis + a formal apparatus + a set of essay drafts**. The essays are the place where that apparatus is supposed to become readable prose.

---

## 2. What an "essay" is here (and what "expansion essay" means)

There is one pipeline with **two generators** and **one publishing gate**.

### 2.1 The two generators

| Kind | File shape | What it actually is | Count |
|---|---|---|---|
| **Expansion essay** | `trika-x/formal-trika/swarm/expansion-*.essay.json` (`expansion-essay/1`) | A machine-compiled draft grown from **one chunk** of the corpus: frozen claims, verbatim verses, tiers, cited Lean theorems, an expansion-graph receipt | **6** |
| **Cross-model essay** ("xmodel") | `swarm/xmodel-*.essay.json` (`trika-essay`) | A machine-compiled comparison between Trika and another formalised theory (Advaita, HOT, IIT, GWT, Madhyamaka, PCM), grown from a **tension** | **6** |

They are not "blog posts with citations". The schema (`trika-x/formal-trika/ESSAY-SCHEMA.md`) forbids anything outside a fixed field set:

- `claims[]` — frozen first, each with `verse_id`, `tier` ∈ {T,R,E,C,H,X}, `kind`
- `verses[]` — frozen at compile; prose may not add verses
- `voice[]` — verbatim owner lines only, never paraphrased
- `theorems[]` — Lean names; **tier UNVERIFIED until registry-checked**
- `tension` — at most one, `resolves` or `loosens`, must resolve via `tension:<id>`
- `receipt[]` — the compile receipt (frozen claim count, orphans must be 0)

The prose is a **separate artifact** (`swarm/<slug>.md`, with `.rev1`, `.rev2`, pushback files). There are 60 such prose files. The compiler never rewrites quotes (compiler law).

### 2.2 The publishing gate (7 stages)

From `trika-x/formal-trika/ESSAY-PIPELINE.md`:

```
0 Source   → pin passages/argmaps/voice/research objects (hashes)
1 Compile  → voice + banked claims + tiers + markers + graph   [receipt]
2 Prose    → v6 passes (Write→Identify→Repair→Texture)
3 Audit    → link_claims + audit_draft (markers resolve, quotes bind)
4 Pushback → interpretive destroy ×2 families
5 Review   → human decision recorded (Scholar)
6 Publish  → signoff → branch → DOI → bibliography listing
```

Fail-closed: a stage that fails blocks downstream. **Machine proposes; human disposes.** No auto-sign, no auto-publish, ever.

### 2.3 Where the current 12 really stand (measured today)

```sh
cd /root/trika-x
python3 formal-trika/tools/essay_check.py     # schema/gate check
python3 formal-trika/tools/essay_derive.py    # claim→verse→trace derivation
```

- `essay_check.py` → **12/12 essays READY_FOR_HUMAN_REVIEW** (schema + tracked + claims frozen).
- `essay_derive.py` → **12/12 BROKEN**, all for the same class of reason:
  - `claim CLM-n has no verse_id` (the claims are not bound to verse IDs), and
  - for some, `no trace bundle for <chunk>`.

This is the single most important sentence in this report:

> The essays pass the *schema* gate and fail the *derivation* gate. They are well-formed drafts, not yet traceable drafts.

That is exactly the gap stage 3 (Audit) exists to catch, and it is fixable mechanically for most claims.

---

## 3. What we can do with them (concrete)

### 3.1 Publish path for the 12 drafts

1. **Bind claims to verses** (`verse_id` per claim). This is the blocker; it is a data-edit pass over `swarm/*.essay.json`, then re-run `essay_derive.py` until PARTIAL/BROKEN → PASS.
2. **Ensure a trace bundle per chunk** (`tal-a34-p01`, `tsa08-p01..p03`, `param-p04`) — all four works are already traced, so most missing-bundle cases are a stale path, not missing data.
3. **Audit + PUSHBACK** (`mcp/scholar_server.py` tools `link_claims`, `audit_draft`, `pushback` in svread). Pushback never edits the draft; it files candidate objections.
4. **Human review** in Scholar: `request_review` → annotations → decision.
5. **Sign + DOI** (Zenodo token is the owner's). No DOI exists yet anywhere in the estate.
6. **Bibliography listing** via the release manifest + `openpatala` work record.

### 3.2 What the two families are *for*

- **Expansion essays** are the "one chunk, one argument" unit. They are the natural **essay-of-record** for a passage. Six exist: `mala-full`, `hook-five-knots`, `node1-tattva`, `worlds-bodies`, `prarabdha-karma`, `nomeans-anupaya`.
- **Xmodel essays** are the comparative unit. They pair Trika with an outside formalism and must name the obstruction when they say "incompatible". Six exist (Advaita, HOT, IIT, GWT, Madhyamaka, PCM).

The missing link, already identified in `ESSAY-TENSION-SCIENCE.md`: expansion essays carry **no tension**, so they float. Wiring each to a `tension:<id>` (11 exist in `svread/data/xmodel/tensions.json`) turns them from isolated drafts into a **research programme** — tension → essay → theorem → span.

### 3.3 The two papers

- `docs/papers/P1-formalising-the-frame-2026-11-17.md` — "Formalising the Frame, Not the Identity" (aperture/inexternalism).
- `docs/papers/P2-trika-in-consciousness-studies-2026-11-17.md` — "Trika in Consciousness Studies: a map of what does not connect".
- `docs/ratie-paper-2026-11-16.md` — HISTORICAL, machine-assembled, explicitly PARTIAL by construction.

Both P1 and P2 are honest drafts ("DRAFT — not peer reviewed, no DOI, no human sign-off"). They are publishable only after the same human gate as the essays. They are, however, the best *readable* statement of the programme and deserve a critical read before any DOI.

---

## 4. The rest of the work that is worth reading/publishing

Measured this session:

| Surface | Number | Where |
|---|---|---|
| Works with translation layers | **95 works / 367 songs** | `svread/data/layers-index.json` (regen: `tools/emit_layers_index.py`) |
| Pinned passage chunks | **239** | `trika-x/formal-trika/bridge/passages.snapshot.json` |
| Lean theorems (public) | **202**, referencing **23/239** chunks | `svread/data/formal.json` |
| EVIDENCE registry | **202 entries over 31 works** | `trika-x/formal-trika/EVIDENCE.json` |
| Trace bundles | **910** (231 COMPLETE / 679 PARTIAL) | `svread/data/traces/index.json` |
| IPVV | 49 chunks, gates PASS, 46/49 verified English | `svread/data/ipvv.json` |
| Cross-model comparisons | **11** (3 incompatible, 1 fit, 5 partial, 2 not-comparable) | `svread/data/xmodel/comparisons.json` |
| Cross-model tensions | **11** | `svread/data/xmodel/tensions.json` |
| Pushing corpus | 115 live questions | `svread/data/pushing.json` |
| Topic pages | 2 (`puryastaka`, `subtle-body`) | `svread/topics/` |

The comparative table is itself publishable material: Trika is the only side that is machine-checked, and every "incompatible" verdict names an obstruction rather than gesturing.

---

## 5. Recommended order of work

1. **Derivation pass** on the 12 essays (bind `verse_id`; re-run `essay_derive.py` to PASS/PARTIAL). *Mechanical, highest value.*
2. **Tension wiring**: attach one `tension:<id>` to each expansion essay (schema already supports it; `ESSAY-TENSION-SCIENCE.md` specifies the rule).
3. **Audit + PUSHBACK** on the three strongest drafts first: `expansion-mala-full` (27 claims), `expansion-nomeans-anupaya` (12), `xmodel-compare-pcm` (9, 3 theorems).
4. **Critical read of P1 + P2** by a named human; then either revise or DOI.
5. **Only then** the DOI/Zenodo and bibliography listing (owner token).

## 6. Limits of this report

- "READY_FOR_HUMAN_REVIEW" is a schema verdict. It is **not** approval, peer review, or a claim of truth.
- The derivation failure is reported as measured today; if the schema was intentionally changed to drop `verse_id`, this report is the place to record that amendment.
- No essay has a DOI. No paper has peer review. Saying otherwise would violate the estate's own laws.
