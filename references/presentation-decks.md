# Presentation And Decks

Use this reference for PPT, HTML decks, demo talks, public reports, proposals, launches, competitions, and any artifact AY may present directly.

## Route The Deck First

| Deck type | Primary job | Quality emphasis |
| --- | --- | --- |
| Technical proof / evaluation | Make a bounded claim credible | Comparable evidence, readable proof, restrained wording |
| Product / decision | Help someone choose a route | Options, tradeoffs, mechanism, risk, next decision |
| Competition / event / brand | Create understanding, energy, and participation | Visual identity, useful density, momentum, memorable rhythm |
| Sponsorship / government / partner | Convert interest into cooperation | Stakeholder value, resource ask, trust, execution path |
| Demo / launch | Make a capability or product feel real | Visible product flow, live rhythm, payoff, recovery path |

Do not apply one deck's restraint, density, or visual system to every other type. If the type is unclear, decide audience, desired belief/action, and setting before touching pages.

## Build Order

1. **Purpose**: the belief, decision, or action the deck must change.
2. **Audience**: role, prior knowledge, objections, attention, and live setting.
3. **Source boundary**: approved facts, assets, screenshots, data, exclusions, and unknowns.
4. **Story spine**: the few beats the audience must follow.
5. **Page jobs**: one communication job per page; multiple modules are allowed when they serve that job.
6. **Visual language**: chosen from project, brand, content, and venue—not from a fixed AY style.
7. **Artifact verification**: rendered pages, live usability, editability, density, and evidence.

An outline is planning, not a finished deck.

## Decision And Time Budget

Before drafting, freeze the requested page range, talk time, audience decisions, and material objections. If no page or time budget was supplied, propose one and label it as proposed rather than silently expanding the artifact.

Keep artifact tiers distinct:

| Tier | Deliverable boundary |
| --- | --- |
| Outline | Story beats and page jobs only |
| Page copy | Titles, on-screen claims, proof, and visual directions within the requested limits |
| Speaker script | Timed spoken narrative, only when requested |
| Rendered artifact | Editable deck or runnable HTML plus rendered inspection evidence |

Do not add a script to page copy, turn an outline into a pseudo-deck, or claim a rendered artifact from prose. Generation runtime is measured from runner events or equivalent logs; page-count and content audits cannot prove runtime efficiency.

Create a compact page-job map before prose:

| decision or objection | one home page/job | evidence or mechanism | allowed cross-reference |
| --- | --- | --- | --- |

Each decision, calculation, condition, or objection gets one primary home. Later pages may point back to it but should not restate the same case with new wording. Repetition is justified only when the live setting requires a recap and the recap has a distinct job.

Budget discipline is not content deletion:

- preserve the evidence, mechanism, resource ask, risk boundary, and post-approval handoff needed for the decision;
- merge or remove pages that do not change belief, decision, objection handling, or execution;
- keep speaker cues compact unless a full script was requested;
- if required content cannot fit the frozen budget, surface the conflict and ask to change scope or budget instead of quietly producing a longer deck.

Verify a mechanical page limit only from actual PPTX slides, explicit HTML `.slide`/`.page` elements, or one `<!-- slide -->` marker per Markdown page. Ambiguous page boundaries are not proof of compliance. Page counting cannot judge repeated arguments, live pacing, or whether essential content was deleted.

## Existing-Deck Revision Gate

Before editing, record what the original already does well. A revision fails if it becomes cleaner but loses useful information, project identity, live usability, editability, or persuasive energy.

Preserve or improve:

| Baseline value | Check |
| --- | --- |
| Information | Mechanism, timeline, proof, resource ask, risk boundary, next decision |
| Live use | The speaker does not need to rebuild basic context verbally |
| Identity | The project, event, product, or partner feels specific |
| Edit use | New evidence and terms can be added without fragile reconstruction |
| Energy | The listener has a reason to care, approve, join, sponsor, or continue |

If a rule-driven revision degrades these, roll it back. Do not defend the rule.

## Real Artifact Gate

For `.pptx`, keynote-style HTML, or a deck used live:

- render or screenshot the original and revision;
- compare page by page;
- inspect hierarchy, contrast, typography, spacing, visual assets, overflow, and projection readability;
- run the core presentation path;
- confirm the file remains editable and the source assets are available.

Without rendered evidence, label the result `outline`, `proposal`, or `unverified deck edit`—not “PPT finished.”

## Source Boundary

| Source | Rule |
| --- | --- |
| User-approved source set | Use the approved directory, logs, data, recordings, images, or prior deck |
| Assistant summary | Working note only unless the user approves it as source material |
| Rejected artifact | Exclude from proof; it may be named only as an excluded experiment |
| Missing visual | Capture or render the relevant state; do not borrow a nearby image |
| Screenshot | Crop to the claim-relevant region and remove unrelated private context |
| Metric | Define source, time window, numerator/denominator, and what it can support |

For public comparisons, keep a short allowlist/exclusion list. Wrong evidence is a stop condition before layout.

## Density And Attention

One page, one job does not mean one sentence or one card. A page may need a timeline, matrix, map, annotated visual, dense comparison, or layered mechanism.

Density is too low when:

- the audience needs a mechanism, timeline, value, proof, resource ask, or next step but sees only a slogan;
- the speaker must add essential context verbally;
- whitespace, rounded cards, or oversized titles replace substance;
- the file cannot absorb new evidence without redesign.

Density is too high when the reading order, claim, and next action disappear. Organize density; do not delete meaning to create calm.

The first attention path should be explicit:

`primary claim -> proof/mechanism -> implication -> next action`

## Visual Standard

- Use the project's real identity: brand assets, product states, venue/event language, photography, texture, diagrams, or motion where appropriate.
- Do not default to generic AI gradients, card grids, fake device frames, or sparse “safe” slides.
- Use color, type, scale, alignment, and grouping to express hierarchy—not decoration.
- Technical proof may be restrained; event, brand, and launch decks may need stronger energy.
- Choose visuals that carry information or identity. Decorative screenshots and random icon piles do neither.

## Audience Voice

Slides speak to the listener, not to the internal production team.

Remove visible scaffolding such as:

```text
最终口径
这里重点看
观众关心什么
点击放大
speaker notes / 讲稿
internal run ids or agent ids
```

State the positive claim directly. Use contrast only when the distinction itself is essential and evidenced. Do not open by explaining what the deck is not.

For proposals, every page should answer at least one:

- Which decision is requested?
- Which resource, permission, or commitment is needed?
- What value and risk control does the listener receive?
- What happens next after agreement?

## Comparison And Evidence

Comparable claims require comparable inputs, windows, states, and source quality. If they differ, lower the claim and state the boundary.

Do not call an untested area a product or model limitation. Use `untested scope`, `cost boundary`, or `verification gap` unless evidence proves a real limit.

Raw page counts, tool calls, build counts, or run ids are not automatically audience evidence. Translate them into a meaningful product, operational, or engineering claim and state what they do not prove.

For continued-collaboration claims, separate:

| Layer | Question |
| --- | --- |
| Initial delivery | What was produced before extensive correction? |
| Completion depth | Which user, function, data, and system layers actually work? |
| Convergence | Does feedback preserve constraints and lead to verified improvement? |
| Harness contribution | What came from model behavior versus tools, scripts, tests, and human guidance? |
| Boundary | What remained untested, costly, unavailable, or incomparable? |

## Screenshots And Demo Logic

Proof screenshots must be relevant, readable, non-duplicate, and tied to the claim. Show comparable states in a useful order, such as `input -> progress -> result/detail`.

Brand/event visuals may also carry atmosphere and identity, but they still need a page job. A screenshot wall without an argument is not proof; a sparse page without identity is not a brand deck.

For product demos, use:

`user situation -> input -> visible product behavior -> result -> boundary -> next action`

## Page-Level QA

For every high-stakes page, check:

| Check | Question |
| --- | --- |
| Job | Which belief, decision, or action moves? |
| Audience value | Why does this listener care now? |
| Evidence | Which source, mechanism, asset, or demonstration supports it? |
| Attention | What is read first, second, and last? |
| Voice | Is it public-facing rather than internal instruction? |
| Density | Is there enough useful information without losing reading order? |
| Risk | What overclaim, ambiguity, or sensitive wording remains? |

Before handoff, render, inspect, and compare. Mechanical checks may catch empty content, obvious internal labels, bad deck types, and text-density regression; they cannot prove the deck is beautiful or ready.
