# Methodology and Limitations

## Design intent

This case study is an operational demonstration, not a claim that a 24-scenario set can establish production model safety. I selected a compact dataset so the full reasoning chain remains inspectable: source row, SQL transformation, dashboard signal, escalation queue, and written decision.

## Dataset construction

- 24 scenario abstractions were paired across a baseline and candidate version.
- Risk domains cover self-harm, privacy/doxxing, sexual safety, violent wrongdoing, fraud/abuse, hate/harassment, healthcare overreliance, and evasion/jailbreak behavior.
- Product surfaces include consumer chat, developer API, and enterprise assistant.
- The dataset includes both refusal-oriented and safe-capability tests so that over-refusal is not treated as success.
- Scenario text is categorical and sanitized. It intentionally omits executable harmful content, personal data, and real user conversations.

## Why the launch gate is conservative

Aggregate metrics are useful for monitoring but can hide localized severe regressions. The gate therefore checks critical failures first, then pass rate and reviewer agreement. The thresholds are declared before analysis. They are illustrative rather than borrowed from any employer or model provider.

## Reviewer agreement

`reviewer_agreement` records whether the initial reviewers reached the same label. It is not a substitute for inter-rater reliability statistics. With a larger evaluation set, I would calculate Cohen's kappa or an appropriate multi-rater measure, stratify by domain and severity, and track disagreement reasons over time.

## What is not represented

- repeated sampling and variance across stochastic generations;
- prompt-level or completion-level content;
- multilingual or multimodal coverage beyond a single abstract localization case;
- tool-use, agentic, or long-context risks;
- evaluator-model bias or automated grading;
- policy-version drift;
- production traffic weighting and prevalence;
- confidence intervals or power analysis;
- secure evidence handling and access controls beyond the written playbook.

## Production next steps

1. Replace categorical rows with a versioned manifest tied to secure test artifacts.
2. Add multiple samples per scenario and track seeds, configuration, and evaluator versions.
3. Build domain-specific gates with policy and product owners.
4. Add statistical uncertainty, refusal-quality measures, and false-positive analysis.
5. Instrument run integrity, missing-pair checks, and automated escalation.
6. Restrict sensitive prompt and completion access while publishing only aggregate decision evidence.
7. Run recurring saturation reviews and adversarial refreshes.

## Interpretation boundary

The project shows transferable operational and analytical capability. It does not represent work performed for Anthropic, a production safety program, or an evaluation of any real Anthropic model.
