# Long-Running Execution

Use this reference only when work must continue across runs, write durable state, coordinate consumers, pause and resume, recover from failure, or clean up temporary state. It is an execution control, not AY's strategy or content identity.

## One Authority

Maintain exactly one authoritative blueprint. Treat it as both plan and authorization boundary. Supporting documents may constrain execution but may not silently expand scope.

The blueprint must name:

- objective and success condition;
- authorized durable targets and runtime-only directory;
- ordered or parallel work items;
- validation command or observable proof;
- pause, resume, checkpoint, and conflict handling;
- failure, recovery, rollback or containment, and cleanup;
- owner or approver for material changes.

If execution needs another durable target or work item, revise the blueprint before writing it.

## Bounded Run Contract

Each run should make one useful, verifiable change and record:

| Field | Requirement |
| --- | --- |
| work item | The bounded authorized unit |
| entry condition | What must be true before starting |
| change | What was actually changed |
| artifact | Durable output or runtime evidence |
| validation | Command, readback, render, or end-to-end proof |
| skipped | Authorized work intentionally not done |
| failure / risk | What failed or remains uncertain |
| next action | The next bounded branch |

Do not let a long run produce only reviews, scores, plans, or logs. Each development loop must change an artifact, behavior path, reusable input, or executable mechanism.

## Activation Is Not Configuration

When durable state must be consumed by another process, distinguish writing from activation:

| consumer class | required scope | owner / approver | durable target | activation method | observed active proof | completion gate | failure signal | rollback / containment | cleanup |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Requirements:

- enumerate materially different consumer classes and the authorized denominator;
- use an activation method such as reload, restart, redeploy, reconcile, auto-refresh, or bounded manual action;
- obtain proof from the consumer runtime, end-to-end behavior, or external outcome, not by rereading the source file;
- do not call the change active until the declared scope has consumer-side proof;
- do not invent rollback for an irreversible action; use containment and authorized forward recovery.

## Failure Order

Evaluate hard stops before aggregate failure budgets. Stop immediately when a required item becomes unreachable, integrity or authorization is breached, or a terminal failure prevents the objective. Percentage budgets may stop earlier but never delay a hard stop, including for a one-item workset.

## Automation Gate

Do not enable recurring automation until the blueprint, write boundary, validation, checkpoint, pause/resume, recovery, and cleanup path are explicit and tested on one bounded run.

## Completion Test

- Did the run make a useful artifact or behavior change?
- Are all durable writes authorized by the blueprint?
- Did the actual consumer observe the change?
- Can execution pause, resume, recover, contain, and clean up?
- Does the run record state what remains risky and what happens next?
