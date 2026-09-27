# Case review quality lab

**A small, reproducible demonstration of documentation review, escalation, and reviewer calibration.**

[Open the interactive case queue](https://clarejordan.github.io/case-review.html)

The operational question: can a reviewer hand off a sensitive case with enough context for the next person to act responsibly? This lab checks 16 fictional, non-graphic case records for missing ownership, incomplete rationale, unresolved disagreement, and evidence gaps. It keeps urgent cases visible even when their documentation is complete.

## Run locally

Python 3.10+; standard library only. No API keys, network calls, or dependencies.

```sh
cd case-review-quality
python review.py
python -m unittest discover -s tests -v
```

The script writes a [review queue](outputs/queue.csv) and [dashboard data](outputs/review.json). Alternate files can be supplied with `--input` and `--output`.

## What the checks mean

| Signal | Follow-up |
| --- | --- |
| Immediate risk flag supplied by reviewer | Urgent human safety review |
| Reviewers disagree without a reasoned adjudication | Resolve disagreement |
| Restriction proposed on partial or unknown evidence | Review evidence before restriction |
| Missing rationale or owner | Complete the case record |
| Reporting route not assessed | Route to an authorized specialist |
| Reporting review needed without an owner | Assign a reporting-review owner |

A named specialist does not prove a report was submitted. A record with no flags is only **documented under this rubric**, not certified safe or correct. Initial reviewer agreement is not accuracy: both reviewers can be wrong. Adjudication does not erase the initial disagreement metric.

## Scope and limits

This is a portfolio simulation, not operational enforcement experience. All records, reviewers, and outcomes are fictional. The code accepts supplied judgments; it does not detect abuse, classify illegal content, make legal determinations, or submit reports. No real child data, harmful imagery, confidential employer information, or live model outputs are included. The rubric is not OpenAI policy and should not be used in production.

My transferable experience is in behavioral health quality, clinical risk review, training, and mandated reporting in a school setting. School reporting experience is distinct from platform reporting and does not establish experience with NCMEC submissions.

## Review notes

See [decision memo](DECISION_MEMO.md) for tradeoffs, limitations, and a proposed validation plan. [Tests](tests/test_review.py) cover invalid inputs, unresolved disagreement, urgency, reporting handoffs, and deterministic output.

Background references: [OpenAI usage policies](https://openai.com/policies/usage-policies/) and [NCMEC CyberTipline](https://www.missingkids.org/gethelpnow/cybertipline). These provide context, not a substitute for approved procedures or legal review.

## Authorship

Created as a portfolio project for Clare Jordan with AI assistance in implementation, drafting, and testing. The synthetic exercise is intended for review and discussion; it does not claim independent engineering authorship or measured workplace impact.
