import csv
import importlib.util
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location("analysis_validation",ROOT/"tools/run_analysis.py")
module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
class ValidationTests(unittest.TestCase):
    def test_empty_regression_queue_has_header(self):
        with tempfile.TemporaryDirectory() as d:
            target=Path(d)/"queue.csv";module.write_csv(target,[],["scenario_id"])
            self.assertEqual(target.read_text().strip(),"scenario_id")
    def test_missing_candidate_rejected(self): self.invalid("missing")
    def test_duplicate_pair_rejected(self): self.invalid("duplicate")
    def test_empty_input_rejected(self): self.invalid("empty")
    def invalid(self,kind):
        with module.DATA_PATH.open() as f:
            reader=csv.DictReader(f);fields=reader.fieldnames;rows=list(reader)
        if kind=="missing": rows=rows[1:]
        if kind=="duplicate": rows.append(rows[0])
        if kind=="empty": rows=[]
        with tempfile.TemporaryDirectory() as d:
            path=Path(d)/"input.csv"
            with path.open("w",newline="") as f:
                writer=csv.DictWriter(f,fieldnames=fields);writer.writeheader();writer.writerows(rows)
            with patch.object(module,"DATA_PATH",path),self.assertRaises(ValueError): module.load_database()
