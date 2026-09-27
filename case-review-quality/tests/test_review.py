import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from review import analyze, build, ROOT

class ReviewTests(unittest.TestCase):
    def setUp(self): self.records=json.loads((ROOT/"data/cases.json").read_text())
    def one(self,**changes):
        r=copy.deepcopy(self.records[2]);r.update(changes);return analyze([r])["records"][0]
    def test_empty_rejected(self):
        with self.assertRaises(ValueError): analyze([])
    def test_duplicate_rejected(self):
        with self.assertRaises(ValueError): analyze([self.records[0]]*2)
    def test_invalid_action_rejected(self):
        with self.assertRaises(ValueError): self.one(reviewer_a="ban_forever")
    def test_boolean_not_truthy_string(self):
        with self.assertRaises(ValueError): self.one(immediate_risk="false")
    def test_missing_field_rejected(self):
        del self.records[0]["owner"]
        with self.assertRaises(ValueError): analyze(self.records)
    def test_urgent_even_with_owner(self): self.assertEqual(self.one(immediate_risk=True)["priority"],"urgent")
    def test_disagreement_needs_reason(self):
        r=self.one(reviewer_b="restrict",adjudication="no_action")
        self.assertIn("Resolve reviewer disagreement",r["flags"])
    def test_resolved_disagreement_still_counts_initial(self):
        r=self.one(reviewer_b="restrict",adjudication="no_action",adjudication_reason="Context reviewed")
        self.assertTrue(r["disagreement"]);self.assertEqual(r["flags"],[])
    def test_second_reviewer_restriction_checked(self):
        self.assertIn("Review evidence before restriction",self.one(reviewer_b="restrict",evidence="partial")["flags"])
    def test_whitespace_owner_missing(self): self.assertIn("Assign case owner",self.one(owner="  ")["flags"])
    def test_reporting_unassessed_requires_review(self):
        self.assertIn("Assess reporting route with authorized specialist",self.one(reporting_review="not_assessed")["flags"])
    def test_agreement_is_not_documentation_quality(self):
        r=self.one(rationale="");self.assertFalse(r["disagreement"]);self.assertTrue(r["flags"])
    def test_build_is_deterministic_and_does_not_mutate(self):
        original=copy.deepcopy(self.records);analyze(self.records);self.assertEqual(original,self.records)
        with tempfile.TemporaryDirectory() as d:
            out=Path(d);build(ROOT/"data/cases.json",out);first=(out/"review.json").read_bytes()
            build(ROOT/"data/cases.json",out);self.assertEqual(first,(out/"review.json").read_bytes())

if __name__ == "__main__": unittest.main()
