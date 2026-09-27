# Decision memo: documentation checks before automation

## Decision

Use deterministic checks to surface records requiring human follow-up. Do not infer whether abuse occurred or automate enforcement from these fields.

## Why these cases

The fixture deliberately includes easy agreement, unresolved disagreement, incomplete evidence, urgent cases with complete handoffs, and prevention resources. This tests workflow distinctions rather than graphic content recognition. Education cases prevent a blanket assumption that any mention of child safety warrants restriction.

## Review sequence

1. Review urgent cases first, following approved emergency procedures in a real operation.
2. Assign missing case and specialist owners.
3. Resolve disagreements using evidence and the applicable policy version; document the reasoning.
4. Review restrictions proposed with incomplete evidence.
5. Confirm outstanding specialist tasks separately. This lab does not track reporting completion.

## Tradeoffs

A conservative queue can increase workload. Urgent flags are supplied by fictional reviewers, so unflagged urgency remains invisible. Free text is checked for presence, not factual quality. A convincing but incorrect rationale passes that check. There is no proof of evidence provenance, access control, retention policy, audit history, duplicate-report detection, or appeal lifecycle.

Initial agreement uses all cases as its denominator, including later-adjudicated cases. Follow-up includes urgent cases and overlaps with the urgent metric. Counts describe this hand-authored fixture, not prevalence, performance, or effectiveness. There is no held-out evaluation set.

## Before any production pilot

Have policy and legal owners define the real rubric, reporting obligations, access controls, and escalation procedures. Validate against independently adjudicated cases, including false positives and missed risk. Measure disagreement by category, incorrect restrictions, missed escalations, time to qualified review, appeal reversals, and reviewer workload. Analyze both overall results and severe failure modes. Establish versioned decisions, audit logs, and rollback criteria before deployment.

## Interview walkthrough

Explain why a completed handoff can still be urgent; why agreement does not establish correctness; why a reporting-review owner is not proof of submission; and how to distinguish a documentation defect from a substantive enforcement error. Review the code and tests before presenting this work as a demonstration of personal technical skills.
