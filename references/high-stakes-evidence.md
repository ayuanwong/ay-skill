# High-Stakes Evidence

Use this reference only when a decision changes money, rights, permission, delivery boundary, compliance, trust, scale, or another hard-to-reverse commitment. It protects the decision; it must not become the public artifact's personality.

## Decision First

Lead with the current decision, decisive reason, unresolved blocker, and bounded next move. Keep the full ledger internal unless the reader needs to inspect it.

Separate confirmed facts, assumptions, inferences, unknowns, and possibly stale facts. No pointer means no current factual authority. If verification is unavailable, downgrade the claim and narrow the authorized action.

## Atomic Claim Gate

Use the smallest complete set of independently true or false claims. Split price, fee, right, permission, quantity, date, service level, and commitment when each can fail separately.

| claim | status | source pointer | supports / does not support | evidence strength | evidence gap | decision effect | next evidence action | stop / counterevidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

Requirements:

- `status` is `confirmed`, `assumption`, `inference`, `unknown`, or `possibly stale`;
- `source pointer` resolves to a link, file, dataset, sample/interview id, screenshot, or `unverified`;
- write both `supports:` and `does not support:` so the nearest material overreach is visible;
- explain why evidence is strong, medium, weak, or unknown;
- tie every row to a decision effect and smallest next evidence action;
- for `assumption`, `unknown`, or `possibly stale`, begin the final cell with `hold:`, `reversible test:`, or `reduce scope:` (or the Chinese equivalents).

A short answer may use fewer decisive claims. It may not merge independently true claims or silently remove their boundary.

## Quantitative Applicability

When a number drives the decision, preserve:

- population or asset set;
- treated, untreated, or comparison condition;
- numerator and denominator;
- time window;
- operating conditions and exclusions.

Do not apply an effect from a treated subset to untreated units, a short window to a permanent state, or one cost basis to a different group without new evidence.

## Threshold Authority

When a numeric or categorical threshold changes go, expand, stop, spend, quality, risk, or rollout, record:

| threshold | decision branch | status | provenance pointer | metric / denominator / window | decision authority | review point | default branch |
| --- | --- | --- | --- | --- | --- | --- | --- |

Use `authorized` only for a binding constraint or an explicitly approved rule frozen before results. A baseline is a comparison anchor, not automatic permission. Otherwise use `proposed`, name the missing authority, and default to hold, reversible test, or reduced scope rather than increased exposure.

## Public Artifact Boundary

Translate the decision into reader-facing language. Do not paste an audit table into a proposal, report, or client message when it interrupts the narrative. Preserve the decision, source boundary, uncertainty, and required confirmation in the visible artifact; keep internal control structure behind it.

## Completion Test

- Are all independently true or false commitments represented?
- Can every confirmed claim resolve to its source?
- Does each source support this exact scope?
- Are unknowns prevented from authorizing spend, permission, publication, or scale?
- Is the public artifact still readable and decision-oriented?
