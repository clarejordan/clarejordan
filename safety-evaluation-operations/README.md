# Safety Evaluation Operations: Launch Readiness Case Study

This independent portfolio project demonstrates how I would turn a small, sensitive safety-evaluation set into a repeatable launch-readiness workflow. It combines operational policy judgment, paired model analysis, SQL, reviewer calibration, escalation logic, and concise decision documentation.

The dataset is synthetic and intentionally non-operational: it contains categorical descriptions of safety tests, not executable harmful prompts, real user data, confidential employer information, or results from any Anthropic model.

## Decision at a glance

**Recommendation: HOLD candidate-1.5.**

The candidate improves aggregate pass rate from **70.8% to 91.7%** and reduces critical failures from two to one. It nevertheless introduces a new critical privacy/doxxing regression on scenario `PR-01`. The launch gate treats any unresolved critical failure as blocking, so aggregate improvement cannot override the regression.

This is the point of the project: a dashboard should support judgment, not replace it.

## What is included

- `data/evaluation_runs.csv` — 48 paired synthetic evaluation results across two model versions, three product surfaces, and eight risk domains.
- `sql/01_schema.sql` — typed SQLite schema and indexes.
- `sql/02_launch_readiness_analysis.sql` — scorecards, product/domain cuts, paired change detection, and launch-gate logic.
- `sql/03_review_queue.sql` — a severity-aware queue for failures, regressions, and reviewer disagreements.
- `tools/run_analysis.py` — a standard-library pipeline that loads the CSV into SQLite and produces dashboard-ready outputs.
- `tests/test_launch_logic.py` — checks for paired coverage, aggregate improvement, regression detection, and launch-gate behavior.
- `outputs/` — reproducible scorecards, the regression queue, and dashboard JSON.
- `EVALUATION_PLAYBOOK.md` — the operating procedure for scoping, running, reviewing, escalating, and refreshing evaluations.
- `LAUNCH_DECISION.md` — the decision memo an operator would send to policy, engineering, and product partners.
- `METHODOLOGY_AND_LIMITATIONS.md` — design rationale, safeguards, known limits, and what would change in production.
- `AUTHORSHIP.md` — transparent description of the human-led, AI-assisted development process.

## Reproduce the analysis

The project uses only Python's standard library.

```bash
python tools/run_analysis.py
python -m unittest discover -s tests -v
```

Expected console result:

```text
HOLD: 48 evaluation records analyzed; 1 regression(s) queued.
```

## Operational design choices

1. **Paired tests before aggregate scores.** Every scenario is run against the baseline and candidate so regressions cannot disappear inside an improved average.
2. **Severity outranks volume.** A single critical failure blocks launch.
3. **Product surface stays visible.** Consumer chat, developer API, and enterprise-assistant behavior can diverge even under one policy.
4. **Reviewer disagreement is work, not noise.** Disagreement creates an adjudication item and a possible rubric update.
5. **Sensitive details are minimized.** Public artifacts describe the risk and expected behavior without publishing harmful test prompts.
6. **Mitigation has an owner and exit criteria.** The decision memo defines what engineering, policy, and evaluation operations must complete before rerun.

## Why this work fits my background

My professional experience is in behavioral health operations, clinical quality, utilization and care management, mental health parity, high-stakes documentation, and escalation under incomplete information. The underlying operating disciplines transfer directly: define the standard, make judgment reproducible, surface edge cases, protect sensitive information, document the decision, and close the loop.

This project does not claim production trust-and-safety experience. It supplies direct evidence of how I apply those disciplines to a model-evaluation workflow while continuing to build technical depth in SQL, data analysis, and dashboard design.
