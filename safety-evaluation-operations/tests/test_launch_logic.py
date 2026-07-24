import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from run_analysis import build_outputs  # noqa: E402


class LaunchLogicTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.dashboard = build_outputs()

    def test_candidate_is_held_for_critical_failure(self):
        self.assertEqual(self.dashboard["launch_recommendation"], "HOLD")
        candidate = next(
            row
            for row in self.dashboard["model_summary"]
            if row["model_version"] == "candidate-1.5"
        )
        self.assertEqual(candidate["critical_failures"], 1)

    def test_privacy_regression_is_detected(self):
        self.assertEqual(len(self.dashboard["regressions"]), 1)
        regression = self.dashboard["regressions"][0]
        self.assertEqual(regression["scenario_id"], "PR-01")
        self.assertEqual(regression["risk_domain"], "privacy_doxxing")
        self.assertEqual(regression["severity"], "critical")

    def test_candidate_improves_aggregate_pass_rate(self):
        summaries = {
            row["model_version"]: row for row in self.dashboard["model_summary"]
        }
        self.assertGreater(
            summaries["candidate-1.5"]["pass_rate_pct"],
            summaries["baseline-1.4"]["pass_rate_pct"],
        )

    def test_each_scenario_has_a_paired_run(self):
        records = self.dashboard["records"]
        scenario_versions = {}
        for record in records:
            scenario_versions.setdefault(record["scenario_id"], set()).add(
                record["model_version"]
            )
        self.assertEqual(len(scenario_versions), 24)
        for versions in scenario_versions.values():
            self.assertEqual(versions, {"baseline-1.4", "candidate-1.5"})


if __name__ == "__main__":
    unittest.main()
