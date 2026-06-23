"""Fictional parity review checklist example.

This script checks whether a structured review record includes expected
sections for a parity/NQTL documentation review. It is a portfolio example,
not legal, compliance, clinical, or operational advice.

Run:
    python parity_review_checklist.py sample_parity_review.json
"""

from __future__ import annotations

import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


REQUIRED_FIELDS = {
    "nqtl_description": "Describe the NQTL in plain language.",
    "benefit_classes": "Identify the benefit classes or service categories in scope.",
    "source_documents": "List plan documents, policies, criteria, workflows, and reports used.",
    "design_factors": "Name the factors used to design the NQTL.",
    "application_factors": "Name the factors used when applying the NQTL.",
    "evidentiary_standards": "Identify evidence supporting each factor.",
    "as_written_comparison": "Compare written M/S and MH/SUD processes.",
    "in_operation_data_plan": "Define data needed to assess operation.",
    "open_questions": "Capture missing evidence, uncertainty, or reviewer follow-up.",
}


@dataclass(frozen=True)
class FieldResult:
    field: str
    status: str
    note: str


def has_meaningful_value(value: Any) -> bool:
    """Return True when a field contains usable content."""
    if value is None:
        return False
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, list):
        return any(has_meaningful_value(item) for item in value)
    if isinstance(value, dict):
        return any(has_meaningful_value(item) for item in value.values())
    return True


def evaluate_record(record: dict[str, Any]) -> list[FieldResult]:
    """Evaluate a structured review record against expected fields."""
    results: list[FieldResult] = []

    for field, guidance in REQUIRED_FIELDS.items():
        if field not in record:
            results.append(FieldResult(field, "missing", guidance))
        elif not has_meaningful_value(record[field]):
            results.append(FieldResult(field, "incomplete", guidance))
        else:
            results.append(FieldResult(field, "present", "Content provided."))

    return results


def print_report(results: list[FieldResult]) -> None:
    """Print a reviewer-friendly summary."""
    total = len(results)
    present = sum(result.status == "present" for result in results)
    needs_review = total - present

    print("Parity review checklist")
    print("=======================")
    print(f"Fields present: {present}/{total}")
    print(f"Needs reviewer follow-up: {needs_review}/{total}\n")

    for result in results:
        marker = "OK" if result.status == "present" else "REVIEW"
        print(f"[{marker}] {result.field}: {result.status}")
        print(f"    {result.note}")


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python parity_review_checklist.py <review_record.json>", file=sys.stderr)
        return 2

    input_path = Path(sys.argv[1])
    with input_path.open("r", encoding="utf-8") as file:
        record = json.load(file)

    results = evaluate_record(record)
    print_report(results)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
