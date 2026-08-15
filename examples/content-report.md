# Case Card: Content Report

Use this case for a reader-facing research report built from surveys, interviews, and external material.

## Source And Status

- Thread: `019f45e6-dca6-7060-99fe-d5f0235c1d51`
- Initial inputs: survey export, questionnaire repository, IMA interview material, and a public interview report.
- Historical status: `no_final_acceptance`. All later observed turns are material corrections; silence after revision is not acceptance.

## Before

The user asked for a user-research analysis report, not a research diary. The sources mixed questionnaire structure, respondent answers, interview evidence, and prior public synthesis.

## Failure Mechanism

The report exposed too much proof process while underperforming on information. It treated questions independently instead of triangulating them, promoted a hierarchy embedded in questionnaire wording into a user-derived finding, and shipped a visible rendering defect.

The failure was not insufficient structure. It was weak separation of evidence, inference, and editorial judgment.

## Better Route

1. Define the reader's decision and the few research questions the report must answer.
2. Separate questionnaire design, respondent evidence, interview evidence, external material, and derived product thinking.
3. Build a private cross-question matrix: supporting signals, contradictions, sample boundary, and what remains unknown.
4. Lead each section with the conclusion; follow with the smallest evidence set that earns it, then state the implication or next decision.
5. Move methodology and proof process to an appendix unless they change trust in a conclusion.
6. Render the real artifact and inspect headings, tables, markup, links, and reading flow before handoff.

When the requested artifact is only a report framework, stop at the narrative architecture and evidence design. A useful shape is one table mapping `reader question → conclusion slot → evidence/comparison → final display`, followed by the comparison matrix and alignment choices. Expanding each proposed chapter into a full checklist is already execution, not framework design.

## Scope And Counterexample

Apply this to research, market, product, and public analysis reports. Do not use brevity to erase sample limits, counterevidence, or uncertainty. A pure source archive may preserve chronology; it should not be mislabeled as an analysis report.

## Current Skill Landing

- Primary route: [`../references/report-writing.md`](../references/report-writing.md).
- Add [`../references/methodology.md`](../references/methodology.md) only when evidence acquisition or research design can change the conclusion.

This is a failure-prevention example, not an accepted model report.
