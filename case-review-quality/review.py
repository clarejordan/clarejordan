"""Offline documentation-quality checks; never an abuse classifier or reporting service."""
import argparse
import csv
import json
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ACTIONS = {"escalate", "restrict", "no_action", "needs_context"}
CATEGORIES = {"child_safety", "privacy", "bullying", "education"}

def analyze(records):
    if not records:
        raise ValueError("At least one case is required")
    seen, reviewed = set(), []
    for r in records:
        required = {"id", "category", "summary", "reviewer_a", "reviewer_b", "evidence", "rationale", "owner", "immediate_risk", "reporting_review", "reporting_owner", "adjudication", "adjudication_reason"}
        if set(r) != required:
            raise ValueError("Case fields do not match the documented schema")
        if any(not isinstance(r[k], str) for k in required - {"immediate_risk"}):
            raise ValueError("Text fields must be strings")
        if type(r["immediate_risk"]) is not bool:
            raise ValueError("immediate_risk must be boolean")
        if not r["id"].strip() or r["id"] in seen:
            raise ValueError("Missing or duplicate case ID")
        seen.add(r["id"])
        if r["category"] not in CATEGORIES or r["reviewer_a"] not in ACTIONS or r["reviewer_b"] not in ACTIONS:
            raise ValueError("Unknown category or reviewer action")
        if r["evidence"] not in {"sufficient", "partial", "unknown"} or r["reporting_review"] not in {"needed", "not_assessed", "not_indicated"}:
            raise ValueError("Unknown evidence or reporting status")
        if r["adjudication"] not in ACTIONS | {""}:
            raise ValueError("Unknown adjudication")
        flags = []
        disagreement = r["reviewer_a"] != r["reviewer_b"]
        resolved = bool(r["adjudication"] and r["adjudication_reason"].strip())
        if disagreement and not resolved: flags.append("Resolve reviewer disagreement")
        if r["adjudication"] and not r["adjudication_reason"].strip(): flags.append("Document adjudication rationale")
        if not r["rationale"].strip(): flags.append("Document review rationale")
        if not r["owner"].strip(): flags.append("Assign case owner")
        action = r["adjudication"] if resolved else r["reviewer_a"]
        if r["evidence"] != "sufficient" and (action == "restrict" or (not resolved and r["reviewer_b"] == "restrict")):
            flags.append("Review evidence before restriction")
        if r["reporting_review"] == "not_assessed": flags.append("Assess reporting route with authorized specialist")
        if r["reporting_review"] == "needed" and not r["reporting_owner"].strip(): flags.append("Assign reporting-review owner")
        if r["immediate_risk"]: flags.append("Urgent human safety review")
        priority = "urgent" if r["immediate_risk"] else "follow_up" if flags else "documented"
        reviewed.append(dict(r, flags=flags, priority=priority, disagreement=disagreement))
    reviewed.sort(key=lambda r: ({"urgent":0,"follow_up":1,"documented":2}[r["priority"]],r["id"]))
    n = len(reviewed)
    return {"dataset":"Fictional training cases v1; no real users or model outputs", "policy_basis":"Portfolio rubric v1; not employer policy or legal advice", "metrics":{"cases":n,"urgent":sum(r["priority"]=="urgent" for r in reviewed),"follow_up":sum(bool(r["flags"]) for r in reviewed),"initial_agreement_pct":round(100*sum(not r["disagreement"] for r in reviewed)/n,1)},"records":reviewed}

def build(source, output):
    result = analyze(json.loads(source.read_text()))
    output.mkdir(parents=True, exist_ok=True)
    (output/"review.json").write_text(json.dumps(result,indent=2)+"\n")
    with (output/"queue.csv").open("w",newline="") as f:
        writer=csv.writer(f)
        writer.writerow(["case_id","priority","owner","follow_up"])
        writer.writerows([r["id"],r["priority"],r["owner"],"; ".join(r["flags"])] for r in result["records"])
    return result

if __name__ == "__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input",type=Path,default=ROOT/"data/cases.json")
    parser.add_argument("--output",type=Path,default=ROOT/"outputs")
    args=parser.parse_args()
    print(json.dumps(build(args.input,args.output)["metrics"],indent=2))
