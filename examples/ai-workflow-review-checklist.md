# Example: AI Workflow Review Checklist

Fictional and sanitized portfolio example. Not clinical, legal, compliance, or operational advice.

## Use Case

A healthcare operations team wants to use AI to support first-pass review of policy or parity documentation. The tool should help organize information and flag missing elements, not make final compliance decisions.

## Principle

AI can help with structure, consistency, and drafting support. It should not replace human ownership of interpretation, judgment, or sign-off.

## Guardrails

- No member-level protected health information in prompts or sample data
- Human reviewer remains accountable for final interpretation
- Output must cite the input section it relied on
- The tool may flag missing information, but may not conclude compliance status independently
- Any uncertainty should be visible, not hidden
- Review logic should be documented in plain language
- Results should be easy for clinical, legal, compliance, and operations partners to challenge

## Intake Questions

1. What document or workflow is being reviewed?
2. What decision is the reviewer trying to support?
3. What source documents are authoritative?
4. What information is missing or uncertain?
5. What output format would help the team act?
6. Who reviews the AI-assisted output before it is used?

## Suggested Output Template

| Field | Purpose |
| --- | --- |
| Review topic | Names the policy, workflow, or documentation area |
| Source summary | Brief summary of what the input says |
| Key elements found | Required elements located in the input |
| Potential gaps | Missing, unclear, or unsupported elements |
| Questions for reviewer | Human follow-up questions |
| Confidence notes | Reasons the output may be incomplete or uncertain |
| Source references | Input sections used to produce the response |

## Example Prompt Pattern

```text
You are helping organize a documentation review. Do not make a final compliance determination.

Task:
Review the provided fictional policy summary and identify whether the documentation includes the required elements listed below.

Required elements:
- NQTL description
- Benefit class or service category
- Factors used in design
- Factors used in application
- Evidentiary standards
- Source documents
- As-written comparison
- In-operation data plan
- Open questions or missing evidence

Output:
Return a table with Found, Missing, Unclear, and Reviewer Follow-Up.
Cite the source section for every item marked Found.
If evidence is missing, say what type of source would help.
```

## Example Human Review Questions

- Did the AI overstate what the source actually supports?
- Did it confuse a factor with an evidentiary standard?
- Did it treat a generic process statement as proof of operational consistency?
- Did it identify missing data without implying failure?
- Would a non-technical reviewer understand the next step?

## Quality Criteria

A useful AI-assisted workflow should be:

- Traceable: reviewers can see where each point came from
- Conservative: uncertainty is not smoothed over
- Repeatable: the same checklist can be reused across documents
- Practical: outputs connect to a next action
- Human-centered: the tool makes review easier without pretending the work is simple

## Why this example matters

The valuable part of AI in healthcare operations is not magic. It is making repeatable work easier to inspect, improving consistency, and giving expert reviewers more time for the judgment calls that actually need them.