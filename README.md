# Clare Jordan, M.Ed., LPCC, NCC

**Safety evaluation operations · behavioral health policy · clinical quality · high-stakes systems**

I am a licensed clinician and operations leader with 15+ years of experience turning risk, policy, and quality expectations into decisions people can execute, review, and improve.

My professional grounding is in mental health parity, clinical quality, utilization and care management, crisis assessment, training, and leadership. My current technical work applies that operating discipline to AI safeguards: paired evaluations, regression triage, reviewer calibration, launch gates, mitigation tracking, SQL analysis, and decision documentation.

[Portfolio](https://clarejordan.github.io/) · [Safety-evaluation dashboard](https://clarejordan.github.io/safety-evaluations.html) · [LinkedIn](https://www.linkedin.com/in/clareljordan) · [Email](mailto:clare.l.jordan@gmail.com)

## Featured build: safety evaluation operations

[**Inspect the complete project →**](./safety-evaluation-operations/)

I built a synthetic, reproducible launch-readiness workflow for a model candidate:

| Signal | Result |
|---|---:|
| Paired scenarios | 24 |
| Total evaluation runs | 48 |
| Candidate pass rate | 91.7% |
| Baseline pass rate | 70.8% |
| New critical regressions | 1 |
| Launch recommendation | **HOLD** |

The candidate fixes six baseline failures and improves overall performance by 20.9 percentage points. A paired SQL comparison also identifies a new critical privacy/doxxing regression. Because the pre-registered gate requires zero unresolved critical failures, the launch remains on hold.

The repository includes:

- a typed SQLite schema and indexed evaluation table;
- SQL scorecards, product/domain cuts, paired regression detection, and a severity-aware review queue;
- a standard-library Python pipeline that generates dashboard-ready outputs;
- automated tests for paired coverage, improvement, regression detection, and launch-gate behavior;
- an evaluation runbook, launch decision memo, mitigation owners, and rerun exit criteria;
- a methodology and limitations statement that separates this portfolio evidence from production experience.

## What I bring to safeguards work

- **High-stakes judgment:** crisis assessment, clinical risk, sensitive content, incomplete information, defensible decisions, and appropriate escalation.
- **Policy-to-operations translation:** mental health parity requirements, NQTL documentation, evidence needs, reviewer guidance, and audit support.
- **Zero-to-one quality systems:** training, QA tools, recurring review cadences, dashboards, and executive-facing decisions for distributed behavioral health operations.
- **Program leadership:** concurrent workstreams, cross-functional delivery, and direct leadership of 17 licensed clinicians.
- **Technical fluency in practice:** SQLite, CTEs, conditional aggregation, self-joins, CSV/JSON pipelines, automated tests, vanilla JavaScript dashboards, and Git-based documentation.
- **Clear limits:** I distinguish transferable operating experience from production trust-and-safety experience and make assumptions visible.

## Additional operating artifacts

- [NQTL documentation map](./examples/nqtl-documentation-map.md)
- [AI workflow review checklist](./examples/ai-workflow-review-checklist.md)
- [Clinical quality training brief](./examples/clinical-quality-training-brief.md)
- [State policy technical assistance one-pager](./examples/state-policy-technical-assistance-one-pager.md)
- [Python parity review checklist](./examples/parity_review_checklist.py)

## How I work

I start with the decision a person must make. Then I define the evidence, severity, reviewer role, escalation path, documentation standard, and feedback loop around it. The goal is not process for its own sake; it is a system that makes important findings harder to miss and easier to act on.

## Authorship and AI collaboration

The featured case study is human-led and AI-assisted. The professional context, constraints, risk framing, requirement for reproducibility, and final accountability belong to me. AI tools accelerated drafting, coding, and consistency checks. The project is explicit about synthetic data, limitations, and the distinction between a portfolio simulation and production trust-and-safety work.

I do not use confidential employer information, real user data, proprietary model results, or executable harmful prompts in this public repository.
