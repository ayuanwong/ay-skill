# Case Card: Product Attention

Use this case when a dashboard or product surface must help a user understand system state and act.

## Source And Status

- Thread: `019ec0f2-27b3-7e92-a354-4b9b0d623c5d`, user turns 11 and 16-18.
- Artifact: course dashboard HTML plus rendered screenshot.
- Historical status: `partial_approval`. Turn 18 approved the layout direction only and named remaining defects; no whole-page final acceptance was observed.

## Before

The forward test existed to check whether AY's product framework and attention-allocation preference changed a real webpage, not whether the page could display a complete set of cards.

## Failure Mechanism

The first page opened on a selected class before answering the teacher's first question: is the overall situation safe, and what needs action now? Revisions still used avoidable scrolling, an unconvincing 80/20 split, redundant Todo modules, an extra click for a deterministic result, and similar visual forms for different cognitive jobs.

The visible symptom was “AI flavor.” The deeper mechanism was missing user-state, decision, attention, and action logic.

## Better Route

1. Name the user state, pressure, primary question, and next action.
2. Rank content by decision value and cognitive cost before choosing layout.
3. Make the first viewport answer system status, items needing attention, and the immediate action.
4. Move from overview to ranked items to detail; keep core metrics and causal background together when the detail must explain a judgment.
5. Remove interactions that add no choice, merge duplicate action surfaces, and give different cognitive jobs different visual forms.
6. Render and inspect desktop and mobile behavior; revise hierarchy before decorative styling.

## Scope And Counterexample

Apply this to dashboards, agent surfaces, and operational product pages. Do not universalize `50/50`, “no scrolling,” pure white, or “no rounded cards.” A consumer, brand, event, or immersive product can need a different visual language.

## Current Skill Landing

- Product route: [`../references/product-attention-framework.md`](../references/product-attention-framework.md).
- Visual production only: [`../references/visual-style.md`](../references/visual-style.md).

Treat the approved layout as a scoped signal, not a finished template.
