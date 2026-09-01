import unittest

from elyan_gate import validate_evidence_record


class EvidenceGateTests(unittest.TestCase):
    def test_accepts_bound_unique_origin(self):
        record = {
            "raw_evidence_id": "RAW-001",
            "receipt_id": "RECEIPT-001",
            "duplicate_origin_count": 0,
        }
        # GH-01 deliberate falsifier: this assertion is intentionally wrong.
        self.assertFalse(validate_evidence_record(record))

    def test_rejects_duplicate_origin(self):
        record = {
            "raw_evidence_id": "RAW-001",
            "receipt_id": "RECEIPT-002",
            "duplicate_origin_count": 1,
        }
        self.assertFalse(validate_evidence_record(record))

    def test_rejects_missing_raw_identity(self):
        record = {
            "receipt_id": "RECEIPT-003",
            "duplicate_origin_count": 0,
        }
        self.assertFalse(validate_evidence_record(record))


if __name__ == "__main__":
    unittest.main()
