DROP TABLE IF EXISTS evaluation_runs;

CREATE TABLE evaluation_runs (
    run_date TEXT NOT NULL,
    eval_id TEXT PRIMARY KEY,
    scenario_id TEXT NOT NULL,
    model_version TEXT NOT NULL,
    product_surface TEXT NOT NULL,
    risk_domain TEXT NOT NULL,
    severity TEXT NOT NULL CHECK (severity IN ('critical', 'high', 'medium')),
    eval_type TEXT NOT NULL,
    expected_action TEXT NOT NULL,
    observed_action TEXT NOT NULL,
    outcome TEXT NOT NULL CHECK (outcome IN ('pass', 'fail')),
    reviewer_agreement INTEGER NOT NULL CHECK (reviewer_agreement IN (0, 1)),
    latency_ms INTEGER NOT NULL CHECK (latency_ms > 0),
    notes TEXT NOT NULL
);

CREATE INDEX idx_eval_model ON evaluation_runs(model_version);
CREATE INDEX idx_eval_domain ON evaluation_runs(risk_domain);
CREATE INDEX idx_eval_scenario ON evaluation_runs(scenario_id);
CREATE INDEX idx_eval_severity_outcome ON evaluation_runs(severity, outcome);
