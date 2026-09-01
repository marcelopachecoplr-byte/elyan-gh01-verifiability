def validate_evidence_record(record: dict) -> bool:
    """Minimal deterministic GH-01 harness.

    A record is accepted only when it binds one physical evidence origin
    (raw_evidence_id) to one durable receipt (receipt_id) and explicitly
    declares that no duplicate source origin was counted.
    """
    required = ("raw_evidence_id", "receipt_id", "duplicate_origin_count")
    if any(key not in record for key in required):
        return False
    if not isinstance(record["raw_evidence_id"], str) or not record["raw_evidence_id"].strip():
        return False
    if not isinstance(record["receipt_id"], str) or not record["receipt_id"].strip():
        return False
    return record["duplicate_origin_count"] == 0
