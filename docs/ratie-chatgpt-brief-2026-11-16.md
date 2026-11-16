# ChatGPT feedback brief for the Ratie paper — 2026-11-16
*Status: HISTORICAL. What to ask ChatGPT about the companion Ratie assembly, what good feedback looks like, and what it cannot do. (2026-11-16.)*

*Goal: this estate is ChatGPT-native — every checkable claim in the paper is
reachable from ChatGPT with no account and no box. ChatGPT is a verifier and
breaker here, never a signer. Its "looks good" is not a review.*

## How ChatGPT reaches the paper
- Public MCP bundle: https://mcp.svatantrya.net/mcp (51 tools, no auth;
  16/16 agent recipes pass live, re-probed 2026-11-16).
- The assembly doc itself (companion file, same date): read it in the reader
  or paste it into the chat. French quotes are pasted text, not live-fetched
  — ChatGPT cannot verify them (see boundary B1).

## Ask 1 — re-run my anchors (paste-ready)
> Using the public Svatantrya MCP: resolve "isvarasiddhi" and
> "paramarthasara"; call scholar__passage_evidence for
> paramarthasara/param-p04-v29; call formal__trace for paramarthasara/param-p04
> and formal__gaps. Report: work_ids + match status, layers + review_state,
> trace verdict + identity hop + theorem count, coverage string + gap_count +
> returned. Flag anything that differs from: EXACT, 7 layers/UNREVIEWED,
> COMPLETE/BOUND/9-theorems-p04, 17/154 + 138.
- Good feedback: a table of observed vs expected with exact observed values,
  plus the verdict_scope caveat (COMPLETE = links present, not correct).
- Bad feedback: "verified" with no observed values quoted.

## Ask 2 — audit my tiers (paste-ready)
> Here are my claims with tiers [paste honesty sheet]. For each: is the tier
> correctly assigned? Rules: T needs a sha-pinned layer span; R is
> reconstruction via named secondary; E is a checkable file/line fact; C is a
> graded convergence; H is interpretation. Flag any R that reads as T.
- Good feedback: per-claim verdicts naming the exact rule applied.
- The paper's known trap: IPK Sanskrit is R (no IPK work entry), never T.

## Ask 3 — break my paper (paste-ready)
> Try to break this assembly: find an invented entity, a hash you cannot
> recompute, a coverage number without its denominator, a fork presented as
> settled, a silent empty success. Report each attempt and what stopped you.
- Good feedback: named attempts with tool calls shown, including failed
  attempts. (The R5 outsider-verify recipe is the model: fetch + sha256sum.)
- Expected outcome: the French layer is unbreakable-by-machine (no frozen
  links) — ChatGPT should SAY that, not pretend to check it.

## Ask 4 — check my structure (paste-ready)
> My template has 7 slots: paradox, rival, pin, converge, diverge, essence,
> close. For each slot: is its required citation present (verbatim+source or
> verse-id+tier)? Name every slot that is missing its citation.
- Good feedback: a 7-row checklist. Missing citations are findings, not prose
  suggestions — ChatGPT must not fill them by inventing quotes.

## Boundaries (ChatGPT cannot do these — asking is an error)
- B1: It cannot verify the French verbatim (R2 book text is not on the public
  surface). Any claim to have "checked Ratie" is a hallucination report.
- B2: It cannot sign, review, approve, or DOI. Writes answer -32001; human
  gates only, always.
- B3: It cannot run essay_derive/pushback or resolve the 17/154-vs-138
  arithmetic — it can only report the mismatch (which is the honest result).
- B4: "Looks good" is not REVIEWED. review_state stays UNREVIEWED until a
  named human signs in the Scholar surface.

## Recording results
- Paste ChatGPT's reply values back against Ask 1's expected row; any drift
  becomes a dated finding (new HISTORICAL doc), never a silent edit.
- Do not edit the assembly on ChatGPT's say-so. The assembly changes only via
  the estate pipeline (compile → check → derive → human sign).
