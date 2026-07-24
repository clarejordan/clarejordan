# Safety Evaluation Operations Playbook

## Purpose

Create a repeatable, reviewable path from a policy risk to a launch decision. The playbook is designed for a small cross-functional team and a high-stakes deadline; it favors clear ownership, paired evidence, and conservative escalation.

## Roles

| Role | Accountable for |
|---|---|
| Evaluation operations | Run integrity, paired coverage, triage, decision log, rerun coordination |
| Policy or domain expert | Risk framing, rubric interpretation, adjudication, policy currency |
| Safeguards engineering | Root-cause analysis, mitigation, instrumentation, technical validation |
| Product owner | Surface-specific context, launch dependency, user-impact decisions |
| Launch decision owner | Final go, conditional go, or hold |

One person may cover more than one role on a small team, but accountabilities should remain explicit.

## Entry criteria

Start a run only when:

- the candidate build and baseline comparator are immutable and named;
- scenario IDs, product surfaces, risk domains, and severity labels are complete;
- expected behavior and scoring rubrics have domain-expert approval;
- sensitive test content has an approved storage and access path;
- run owners, adjudicators, and the launch decision owner are assigned;
- the launch gate is documented before results are visible.

## Run procedure

1. **Freeze the manifest.** Record model versions, configuration, evaluator version, policy version, dataset version, and timestamp.
2. **Validate coverage.** Confirm paired baseline/candidate rows and at least one critical or high-severity scenario for each in-scope risk domain.
3. **Execute deterministically where possible.** Preserve configuration and retry rules. Log infrastructure failures separately from model-behavior failures.
4. **Score independently.** Two reviewers score critical cases and ambiguous cases without seeing each other's labels.
5. **Triage in order.** Critical failures, regressions, other failures, reviewer disagreement, then unexpected latency or refusal patterns.
6. **Adjudicate.** Resolve disagreements using the written rubric. If the rubric cannot resolve the case, mark it as a policy gap rather than forcing consensus.
7. **Analyze paired changes.** Review every baseline pass/candidate fail before relying on aggregate metrics.
8. **Apply the gate.** Do not relax thresholds after results are known. Any exception requires named decision-owner approval and written rationale.
9. **Publish the decision memo.** Include scope, result, unresolved risks, owners, mitigation, rerun criteria, and evidence links.
10. **Close the loop.** Add newly discovered behavior to the evaluation set and record why it is likely to remain high-signal.

## Launch gate

| Signal | Threshold | Result if missed |
|---|---:|---|
| Unresolved critical failures | 0 | Hold |
| Candidate pass rate | At least 90% | Conditional hold |
| Reviewer agreement | At least 90% | Conditional hold and calibration |
| Paired scenario coverage | 100% | Invalid run |
| Critical regression review | 100% adjudicated | Hold |

The gate is deliberately simple enough to audit. Production use would add domain-specific thresholds, statistical power, variance across samples, and automated integrity checks.

## Escalation levels

### P0 — critical launch blocker

Use for an unresolved critical failure, a critical regression, leaked restricted content, corrupted run provenance, or a result indicating broad policy bypass. Notify the decision owner, policy, engineering, and affected product lead immediately. Pause downstream approval.

### P1 — material safety or quality risk

Use for repeated high-severity failures, a concentrated product-surface regression, or material reviewer disagreement. Create a mitigation owner and required rerun before broad release.

### P2 — bounded improvement

Use for isolated medium-severity errors, documentation gaps, or calibration opportunities that do not change the current launch decision. Track to closure with a target release.

## Keeping the set high-signal

- Retire or harden tests that repeatedly pass without discriminating between model versions.
- Convert discovered regressions into stable paired tests after policy review.
- Add product-specific variants when the same intent behaves differently across surfaces.
- Track saturation by domain and eval type, not only across the whole set.
- Separate safe capability tests from refusal tests so over-refusal remains visible.
- Review taxonomy and adversarial patterns on a fixed cadence and after material policy or model changes.

## Documentation standard

Every run should make it possible for a new operator to answer five questions without oral context:

1. What exactly was tested?
2. Which policy or risk standard applied?
3. What changed from baseline?
4. Why did that result lead to this launch recommendation?
5. What must happen next, who owns it, and what evidence closes the item?
