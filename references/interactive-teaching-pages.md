# Interactive Teaching Pages

Use this reference when the user asks for a teaching page, explainer, simulator, lab, guided exercise, or learning tool.

## Learning Contract

Before designing the page, define:

- who is learning and what they already know;
- the concept or decision they should understand afterward;
- the misconception or failure the interaction should expose;
- what observable action proves learning.

Do not add interaction for spectacle. Every control should let the learner test, manipulate, compare, practice, or receive feedback.

## Content Rhythm

A useful sequence is:

1. plain-language model;
2. precise definition;
3. manipulable example or visual explanation;
4. guided exercise;
5. feedback and correction;
6. transfer task or short quiz.

Change the sequence when the topic needs exploration before explanation. Avoid turning the page into a styled article with one decorative button.

## Interaction Options

| Interaction | Best for | Required behavior |
| --- | --- | --- |
| Sort / match / drag | Sequence, grouping, mapping | Clear target, feedback, reset |
| Simulator | Process, system, tradeoff | State-driven controls, visible consequence, reset |
| Comparison | Alternatives and mechanisms | Same variables, clear difference, explanation |
| Sliders / parameters | Sensitivity and thresholds | Live output, units/ranges, meaningful defaults |
| Guided choices | Diagnosis and decision paths | Step state, correction, result rationale |
| Quiz | Retrieval and misconception check | Immediate feedback and explanation |
| SVG/canvas | Spatial, dynamic, or quantitative concept | Legible labels, controls, accessible fallback |

## Deliverable

For a standalone task, prefer a single HTML file with inline CSS/JS when it keeps the artifact easy to open and share. In an existing app, use the project stack and design system.

Choose navigation, width, sidebar, typography, and visual language from the topic and learner—not from a fixed teaching-page template.

## State And Accessibility

- Make selected, correct, incorrect, completed, reset, and disabled states distinct.
- Support keyboard and touch for core interactions where feasible.
- Keep labels and feedback readable on mobile.
- Do not rely only on color to communicate correctness or state.
- Preserve learner progress when navigation or multi-step flow makes that useful.
- Explain why an answer is wrong; a red border alone does not teach.

## Verification

Before handoff:

- open the page in a browser;
- run every core interaction from start to completion;
- test reset and an incorrect path;
- inspect mobile width and overflow;
- check console errors;
- confirm the interaction teaches the promised concept rather than only animating it.

A text-only page, broken control, or interaction without feedback is not an interactive teaching deliverable.
