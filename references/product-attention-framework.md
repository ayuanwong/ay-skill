# Product Attention Framework

A product is a service system. An interface is an attention and action allocation mechanism.

Do not start with modules, cards, metrics, or a visual style. Start with the user's situation and first decision.

## Product Frame

| Layer | Question |
| --- | --- |
| User state | Who is using it, in what situation, under what pressure? |
| Input | What intent, information, data, or material enters? |
| Service | What work does the product perform that the user cannot or should not do alone? |
| Output | What does the user receive, decide, publish, learn, or hand off? |
| Next action | What happens immediately after the output? |
| Boundary | What is explicitly not done, not automated, or not promised? |

If the answer is mainly a feature list, the product is not framed yet.

## Service Reality

Before planning a product surface, define:

- current alternative and switching friction;
- stakeholders and handoffs;
- supply, demand, trust, and compliance constraints;
- private resources: channel, customer access, data, assets, budget, accounts, permissions;
- cost, cycle time, use/adoption, payment/repeat, fail signal, and review input.

Unknown resources are validation tasks, not harmless blanks.

## Attention Map

Use this before layout:

| Item | Meaning |
| --- | --- |
| Primary question | What must the user understand first? |
| Primary action | What should the user do next? |
| Attention budget | How much time and focus are available? |
| Content inventory | What information could appear? |
| Decision value | Which content changes a choice or action? |
| Cognitive cost | How hard is it to understand or verify? |
| Visual weight | What should be large, small, grouped, progressive, or hidden? |
| Interaction | What can be inspected, changed, compared, confirmed, or simulated? |

Rank content by:

`attention priority = decision value / cognitive cost`

Low-priority content becomes secondary, collapsed, deferred, or removed.

## Choose The Page Level

| User's first decision | Start with |
| --- | --- |
| Is the whole system okay? | Overview and next actions |
| Which item needs attention? | Ranked list/table, then detail |
| What happened inside one item? | Detail with enough surrounding context |
| What should I choose? | Comparable options and tradeoffs |
| What must I confirm? | A distinct confirmation state and consequence |

Do not open on one selected detail when the user first needs system status. Do not shrink the main explanation into a narrow side rail.

## Product States

For agentic or asynchronous products, distinguish:

| State | Product responsibility |
| --- | --- |
| Initial | Show relevant state without blocking a new intent |
| Input | Make mode, constraints, and editable context clear |
| Working | Reduce uncertainty; show meaningful progress and allow interruption when safe |
| Needs confirmation | Ask only for the blocking decision; make consequence and risk explicit |
| Result | Use a task-fit surface, with next action and correction path |
| Blocked/error | Explain what failed, what remains safe, and how to recover |
| Multi-task | Separate active, blocked, and completed work without overloading the home surface |

High-risk actions—payment, booking, publishing, deletion, irreversible account changes, or contacting others—need explicit confirmation.

The user's task determines display grammar. A timeline, comparison, document, profile, map, table, preview, or simulator may be better than another chat card.

## Interaction Rules

- Do not add a click for a deterministic result already known from current data.
- Do not split one next action across “priority”, “todo”, and “next step” modules.
- Use progressive disclosure for real depth, not to hide the main judgment.
- Show empty, loading, error, permission, and recovery states when they can occur.
- Keep motion quiet unless it explains state or supports the task.
- Make the core path usable on mobile when mobile use is plausible.

## Layout And Content Forms

The first viewport should answer:

1. Where am I and what state is this?
2. What matters now?
3. What can I do next?

Different cognitive jobs need different forms. A judgment band, comparison table, action list, evidence panel, and detail explanation should not all look like identical cards.

Avoidable scrolling is a product smell in dense desktop tools. First fix loose spacing, repeated modules, and weak hierarchy; keep scrolling only for real depth.

## Deliverable Gate

If the user asks to build a page, app, demo, dashboard, or tool, deliver the runnable artifact when feasible. Advice-only is complete only when advice was requested.

Before handoff, verify:

- initial load and core interaction;
- empty, loading, error, permission, and recovery states;
- responsive/mobile use where relevant;
- visual hierarchy and reading order;
- the real next action;
- source data and claim boundaries;
- no generic template or placeholder interaction is being presented as product quality.

Render or open the artifact when visual quality matters. Source code and clean structure alone do not prove the product surface works.
