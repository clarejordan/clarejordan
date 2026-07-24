-- Prioritized reviewer queue for candidate failures, regressions, and disagreements.
WITH paired AS (
    SELECT
        candidate.eval_id,
        candidate.scenario_id,
        candidate.risk_domain,
        candidate.severity,
        candidate.product_surface,
        candidate.outcome AS candidate_outcome,
        candidate.reviewer_agreement,
        candidate.observed_action,
        candidate.notes,
        baseline.outcome AS baseline_outcome
    FROM evaluation_runs AS candidate
    JOIN evaluation_runs AS baseline
      ON baseline.scenario_id = candidate.scenario_id
     AND baseline.model_version = 'baseline-1.4'
    WHERE candidate.model_version = 'candidate-1.5'
),
flagged AS (
    SELECT
        *,
        CASE
            WHEN severity = 'critical' AND candidate_outcome = 'fail' THEN 1
            WHEN baseline_outcome = 'pass' AND candidate_outcome = 'fail' THEN 2
            WHEN candidate_outcome = 'fail' THEN 3
            WHEN reviewer_agreement = 0 THEN 4
            ELSE 5
        END AS queue_priority,
        CASE
            WHEN severity = 'critical' AND candidate_outcome = 'fail' THEN 'critical failure'
            WHEN baseline_outcome = 'pass' AND candidate_outcome = 'fail' THEN 'regression'
            WHEN candidate_outcome = 'fail' THEN 'candidate failure'
            WHEN reviewer_agreement = 0 THEN 'adjudication'
        END AS queue_reason
    FROM paired
)
SELECT
    queue_priority,
    queue_reason,
    eval_id,
    scenario_id,
    risk_domain,
    severity,
    product_surface,
    baseline_outcome,
    candidate_outcome,
    observed_action,
    notes
FROM flagged
WHERE queue_priority < 5
ORDER BY queue_priority, scenario_id;
