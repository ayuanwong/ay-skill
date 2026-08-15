# Feedback To Skill

Use this reference when AY's correction, praise, dissatisfaction, example, or principle may change `ay-skill`.

The objective is to reduce future explanation burden by changing behavior. A longer review, a larger rubric, or a new rule that never changes an artifact is not progress.

## Evidence Intake

Before changing the skill, capture only what is needed to make a bounded edit:

| Field | Requirement |
| --- | --- |
| Source | AY's actual feedback, artifact, thread, or file—not only an assistant summary |
| Task and user | What was being made, for whom, and in what real use state |
| Failure mechanism | The narrow behavior that caused rework, not only the visible symptom |
| Smallest reusable change | The least instruction, route, reference, asset, or script change that can alter behavior |
| Scope and counterexample | Where it applies and one nearby task it must not distort |
| Observable proof | The cheapest artifact or behavior check that can falsify the proposed repair |

If the original source, failure mechanism, scope, counterexample, or observable proof is missing, keep the lesson in the current task or run log. Do not promote it into the skill yet.

## Label The Turn And Acceptance Scope

Before treating a historical turn as correction evidence, label it:

| Label | Meaning |
| --- | --- |
| `initial_request` | The original job, materials, audience, and constraints available to the first attempt. |
| `material_correction` | Rework that changes the strategy, mechanism, content hierarchy, artifact, or user outcome. |
| `clarification` | Necessary information that could not safely be inferred from the initial request. |
| `new_scope` | A later request that adds a deliverable, audience, constraint, or decision not present initially. |
| `partial_approval` | Approval of one page, section, visual, or mechanism only. Record the approved scope. |
| `final_acceptance` | Explicit acceptance of the whole declared artifact or task boundary. |
| `continuation` | “Continue”, status requests, or process steering with no quality judgment. |

Do not count clarification or new scope as first-pass failure. Do not treat continuation, silence, assistant-declared completion, or partial approval as final acceptance. When no final acceptance exists, record `no_final_acceptance`; use the case for failure prevention, not as a positive exemplar.

## Choose The Destination

| Level | Destination | When justified |
| --- | --- | --- |
| L0 | Current artifact only | One-off wording, project detail, transient preference, or unproven reaction |
| L1 | Run log | Useful case lesson whose transfer boundary is not yet clear |
| L2 | Cognition store | Durable AY belief, taste, resource pattern, or collaboration principle |
| L3 | Scoped reference or reusable asset | A domain workflow or production mechanism with a clear boundary and counterexample |
| L4 | Main skill or deterministic script | A cross-domain behavior supported by multiple task families or an explicit AY-wide principle; scripts require a repeated, harmful, machine-detectable failure |

Do not use review intensity as a promotion signal. Strong dissatisfaction identifies damage; it does not prove universal scope.

## Fast Iteration Loop

Use one short loop at a time:

1. take the latest real correction or failed artifact;
2. choose one failure mechanism that materially changes quality;
3. edit the smallest behavior surface, preferring deletion, narrowing, route splitting, or a reusable production mechanism over another global rule;
4. apply the change immediately to the source task family or a representative deterministic fixture;
5. if the target defect remains, revise in the same loop rather than opening a new review phase;
6. run one counterexample when the change could affect another task family;
7. record what changed, what behavior moved, what remains unproven, and the next action.

Default budget: one behavior hypothesis, one implementation, one targeted proof, and one counterexample. Do not add an evaluator unless the existing artifact check cannot distinguish the target failure. Reserve multiple independent reviewers and broad held-out suites for an actual release candidate, not every development edit.

A loop has not advanced when no artifact, behavior path, reusable asset, or executable mechanism changed.

## Change Rules

- Keep `SKILL.md` for triggers, routing, cross-domain quality behavior, and red lines.
- Put domain detail in one reference; do not duplicate it across the skill.
- Prefer a reusable input, template, asset, or execution step when prose is already correct but behavior still fails.
- Add scripts only for stable structure or runtime failures, not for subjective quality vocabulary.
- Treat keyword and schema checks as coarse guards, never as proof of usefulness or taste.
- Once a prompt or artifact influences a skill change, treat it as development/regression evidence rather than fresh proof.

## Proportional Damage Test

- For a scoped domain change, check the source family and one counterexample.
- For a cross-domain core change, add one short non-source task family where the behavior should transfer.
- If the trigger or route boundary changes, add a routine-code non-trigger check.
- If visual production changes, inspect rendered before/after artifacts; do not substitute source text or lint.
- If a deterministic script changes, run a representative positive fixture and the failure it is meant to catch.

Increase validation only when the change is broader, harder to reverse, or capable of hiding damage. Do not require four large reviews for a narrow, reversible behavior edit.

## Record

The current run log should name the source, failure mechanism, destination, files changed, counterexample, targeted proof, remaining uncertainty, and next action. Keep the record shorter than the work it explains.
