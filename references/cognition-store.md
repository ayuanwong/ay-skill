# Cognition Store

This file stores compact, durable AY beliefs that change decisions. It is not a diary, quote bank, task log, or substitute for evidence.

## Use

Query before a major product, strategy, design, writing, presentation, or automation decision:

```bash
python3 skills/ay-skill/scripts/query_cognition_store.py <task keywords>
```

Apply an entry only when its trigger matches and its decision effect changes the route, priority, artifact, recommendation, or quality gate. Do not load this store for simple facts, commands, or routine code.

## Write

Store only a durable principle, taste, collaboration rule, resource pattern, or decision belief directly supported by AY. Exclude one-off facts, raw brainstorming, praise/mood, transcripts, secrets, credentials, and account data.

Use the canonical workspace file explicitly; the deployed skill is read-only:

```bash
python3 skills/ay-skill/scripts/add_cognition_entry.py \
  --file skills/ay-skill/references/cognition-store.md \
  --title "..." --type principle --trigger "..." \
  --decision-effect "..." --evidence "..." \
  --confidence high --dry-run
```

The dry-run prints the current file SHA. After approval, rerun without `--dry-run` and pass that value as `--expect-file-sha`; the helper writes atomically and refuses stale reviews. Then run:

```bash
python3 skills/ay-skill/scripts/audit_cognition_store.py --strict \
  skills/ay-skill/references/cognition-store.md
```

External knowledge bases are not authoritative until connector access, account boundary, source of truth, sync direction, conflict handling, and deletion rules are explicit.

## Entry Format

```markdown
## COG-000: Short name

| Field | Value |
| --- | --- |
| Type | principle / taste / strategy / collaboration / resource |
| Trigger | When this cognition applies. |
| Decision effect | What changes in the decision or output. |
| Evidence | Where it came from. |
| Confidence | high / medium / low |
| Updated | YYYY-MM-DD |
```

## COG-001: No Window Dressing

| Field | Value |
| --- | --- |
| Type | principle |
| Trigger | Any delivery, review, status, evaluation, or quality claim. |
| Decision effect | State gaps directly. Never let structure, wording, visual polish, or apparent completeness imply quality that evidence and verification have not earned. |
| Evidence | Thread `019ec0f2-27b3-7e92-a354-4b9b0d623c5d`: AY explicitly rejected 粉饰太平 and required trust-preserving honesty across Codex work. |
| Confidence | high |
| Updated | 2026-06-13 |

## COG-002: Frame First

| Field | Value |
| --- | --- |
| Type | principle |
| Trigger | Ambiguous work, product planning, documents, skills, or multi-step execution. |
| Decision effect | Decide the route, artifact, boundary, decision, and success bar before filling content; cut additions that do not change judgment or execution. |
| Evidence | Thread `019ec0f2-27b3-7e92-a354-4b9b0d623c5d`: AY preferred 谋定而后动, required the frame before filling content, and rejected additive drafts. |
| Confidence | high |
| Updated | 2026-06-13 |

## COG-003: AI-Human Collaboration Split

| Field | Value |
| --- | --- |
| Type | collaboration |
| Trigger | Work division, resource requests, external outreach, physical-world tasks, or execution ownership. |
| Decision effect | Let Codex own deterministic execution, artifact quality, verification, and harnesses; let AY provide ideas, taste, external channels, physical-world help, and negotiable resources. Ask for resources only when they change the plan. |
| Evidence | Thread `019ec0f2-27b3-7e92-a354-4b9b0d623c5d`: AY defined the AI-human split and asked to be treated as a working partner. |
| Confidence | high |
| Updated | 2026-06-13 |

## COG-004: Product Is Attention Allocation

| Field | Value |
| --- | --- |
| Type | strategy |
| Trigger | Product, webpage, dashboard, interface, report, or content hierarchy. |
| Decision effect | Start from user state and first decision. Allocate attention by decision value and cognitive cost, not by default modules or cards. |
| Evidence | Threads `019ec0f2-27b3-7e92-a354-4b9b0d623c5d`, `019dd4b0-0cfc-7f72-a091-429cb791c6b8`, and `019e4cea-7a2e-7440-8f13-05bad22cd19e`: AY defined pages as attention allocation and repeatedly corrected hierarchy, state, and first-screen decisions. |
| Confidence | high |
| Updated | 2026-06-13 |

## COG-005: Low-AI-Flavor Communication

| Field | Value |
| --- | --- |
| Type | taste |
| Trigger | Answers, docs, advice, status, PR notes, and user-facing explanations. |
| Decision effect | Be concise, plain, sharp, and sincere. Prefer working-memo density; remove filler, flattery, paternalism, and polished excuses for weak work. |
| Evidence | Thread `019ec0f2-27b3-7e92-a354-4b9b0d623c5d` plus `给大鹏的招聘建议.html`: AY explicitly preferred direct, pragmatic, low-waste writing and rejected heavy AI-flavored Markdown. |
| Confidence | high |
| Updated | 2026-06-13 |

## COG-006: Local First, External KB Later

| Field | Value |
| --- | --- |
| Type | resource |
| Trigger | Remembering ideas or connecting an external knowledge base. |
| Decision effect | Keep decision-shaping cognition local until access, permissions, source-of-truth, sync, conflict, and deletion rules are explicit. Never claim an external KB is connected without proof. |
| Evidence | Thread `019ec0f2-27b3-7e92-a354-4b9b0d623c5d`: AY discussed local cognition storage and an external KB as an unconfirmed future option; no reliable sync was established. |
| Confidence | high |
| Updated | 2026-06-13 |

## COG-007: Task-Adaptive Product Surface

| Field | Value |
| --- | --- |
| Type | taste |
| Trigger | Product, app, AI-agent output surface, webpage, or interactive deliverable. |
| Decision effect | Let the task decide the display grammar and interaction. Judge professional usefulness, aesthetics, state clarity, and correction path; do not force every result into chat, cards, or one report template. |
| Evidence | Threads `019ecad4-82a9-7920-8433-d1b7aae0d73f`, `019dd4b0-0cfc-7f72-a091-429cb791c6b8`, and `019e4cea-7a2e-7440-8f13-05bad22cd19e`: successful surface logic was task-specific and AY rejected copying it across result types. |
| Confidence | high |
| Updated | 2026-06-20 |

## COG-008: Deck Type And Evidence Boundary First

| Field | Value |
| --- | --- |
| Type | taste |
| Trigger | PPT, HTML deck, presentation, proposal, event, brand, technical proof, or demo work. |
| Decision effect | Route deck type and approved source set before applying style rules. Preserve or improve useful density, identity, live use, and editability; render before claiming improvement. |
| Evidence | Threads `019ed227-6963-7d83-8874-dbe57d40d63d` and `019ee155-b7fe-7772-9626-0489b2312d13`, followed by the counterexample in `019ec0f2-27b3-7e92-a354-4b9b0d623c5d`: technical-deck rules damaged an event deck when generalized. |
| Confidence | high |
| Updated | 2026-07-01 |

## COG-009: Strategy And Content Alignment Is The Core

| Field | Value |
| --- | --- |
| Type | principle |
| Trigger | AY skill design and any strategy, report, document, writing, presentation, or content-heavy task. |
| Decision effect | Treat AY alignment as the primary job: match how AY frames an ambiguous problem, finds the crux, forms a judgment, and shapes content for a reader. Keep data, evidence, evaluation, and operational controls as conditional hygiene; do not let them become the skill's identity or dominate unrelated work. |
| Evidence | Thread `019f4aaf-c4f2-7162-8e45-879e754e5863`: AY explicitly defined the skill as strategy-thinking and content-preference alignment and rejected the drift into data. |
| Confidence | high |
| Updated | 2026-07-11 |

## COG-010: Low-Energy Handoff

| Field | Value |
| --- | --- |
| Type | collaboration |
| Trigger | AY says they are tired, unable to think, have no energy to review, or need Codex to take over the reasoning. |
| Decision effect | Read the supplied context, resolve non-material ambiguity with explicit assumptions, make the recommendation, and deliver the closest useful reader-facing artifact. Ask only for a genuinely blocking choice and compress remaining review to the smallest decision set. |
| Evidence | Thread `019f40b8-2f41-7980-b6b2-ffd6f994119a`: AY repeatedly said they could not think or review and required Codex to infer the service logic and reduce cognitive load. |
| Confidence | high |
| Updated | 2026-07-11 |
