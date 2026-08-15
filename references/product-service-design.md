# Product Service Design

Use this reference for product strategy, service design, product planning, and interface architecture. Derive the product from the service system before naming features or drawing pages.

## Contents

Stakeholders | Supply and demand | Business chain | Events and branches | Node inputs/outputs | Functional responsibility | Pages/states | Attention

## Follow The Derivation Chain

Work in this order:

`stakeholders -> supply and demand -> business chain -> events and branches -> node inputs and outputs -> functional responsibility -> pages and states -> attention allocation`

Do not skip from a user problem to a feature list. A feature is justified only when its place in this chain is clear.

## Map Stakeholders And Value

Identify distinct roles even when one person holds several:

- beneficiary or end user;
- buyer, payer, or budget owner;
- supplier or service provider;
- operator or coordinator;
- decision maker, approver, or gatekeeper;
- reviewer, regulator, partner, or risk bearer.

For each relevant role, state the situation, desired change, current alternative, value received, contribution or resource supplied, decision right, incentive, trust requirement, and failure exposure. Do not collapse buyer, user, approver, and operator into a generic "user."

## Define Supply And Demand

Describe the exchange rather than calling the product a platform:

| Question | Requirement |
| --- | --- |
| Demand | Who needs what outcome, in which situation, with what urgency, budget, and acceptance condition? |
| Supply | Who or what can deliver it, with what capacity, quality variance, cost, and constraint? |
| Match | Which attributes determine fit, qualification, priority, and rejection? |
| Trust | What evidence, permission, guarantee, review, or recovery makes exchange possible? |
| Scarcity | Which side, resource, permission, or coordination step is the real bottleneck? |
| Continuity | What produces completion, repeat use, renewal, or a safe exit? |

Distinguish lack of demand from poor access, weak trust, bad matching, missing supply, and broken fulfillment. Each diagnosis implies a different product route.

## Draw The Business Chain

Trace the work from trigger to durable outcome. Use only stages the service actually needs, such as:

`trigger -> access/acquisition -> intake -> qualification -> match or plan -> commitment -> delivery -> acceptance -> settlement -> follow-up/repeat`

For every stage, name:

- the acting role and decision owner;
- the entry condition and input;
- the work or value transformation;
- the output and receiving role;
- the handoff, time, cost, and dependency;
- the failure signal and recovery or exit.

Expose where work currently happens through chat, spreadsheets, memory, manual coordination, or an external service. Productization should remove a decisive friction, not merely redraw existing work on a screen.

## Model Events And Branches

Do not design only the happy path. Include events that change responsibility or state:

- new intent, incomplete or conflicting input;
- unavailable or unsuitable supply;
- permission, trust, payment, or risk block;
- user change, cancellation, interruption, or timeout;
- delivery failure, dispute, correction, or refund;
- completion, handoff, repeat, renewal, or exit.

For each event define:

`current state -> event -> decision -> responsible actor -> action -> resulting state -> recovery or fallback`

Separate true business branches from display variations. A branch earns product logic when it changes rights, work, risk, commitment, or the next decision.

## Specify Node Inputs And Outputs

For each decisive node, state:

| Field | Requirement |
| --- | --- |
| Input | Origin, format, completeness, authority, freshness, and permission to use. |
| Decision or work | Rule, human judgment, transformation, or coordination performed. |
| Output | Artifact, state change, recommendation, commitment, or handoff produced. |
| Consumer | Who uses the output and which next decision it enables. |
| Exit condition | What proves the node is complete. |
| Failure path | What remains safe, who is notified, and how work resumes or exits. |

An output that no later actor or decision consumes is probably process residue. An input with no reliable origin or authority is a validation task, not a hidden assumption.

## Assign Functional Responsibility

Turn a service need into a function only when it reduces material uncertainty, friction, cost, delay, or risk at a named node. For each function define:

- responsible actor: user, system, operator, supplier, partner, or approver;
- mode: automatic, suggested, editable, confirmed, manually operated, or unsupported;
- input and output contract;
- decision right and permission boundary;
- exception, escalation, correction, and recovery path;
- reason this function belongs in the product rather than an operating process.

Do not automate a missing policy or invent authority. High-risk commitments require an explicit confirmation state with consequence visible.

## Derive Pages And States

Create a page or surface around a user question and action in a specific state, not around an internal data entity. Map:

`role + situation + current state -> primary question -> needed information -> available action -> next state`

Distinguish initial, input, working, blocked, needs-confirmation, result, error/recovery, and completed states when they can occur. Keep cross-role views separate when their questions, rights, or actions differ. Do not force every node into a dashboard or every result into a chat card.

## Allocate Attention Last

After the service, responsibility, and state maps are stable, use `product-attention-framework.md` to decide hierarchy and interaction. Rank visible content by decision value relative to cognitive cost. The first viewport should show the current state, what matters now, and the real next action; secondary evidence, history, and uncommon controls can be progressively disclosed.

Before building, verify that every major page and feature traces back to a service node, event, responsibility, or decision—and that the product has an explicit point of view about what it will not do.
