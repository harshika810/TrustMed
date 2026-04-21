import json
import hashlib


def generate_hash(report: dict) -> str:
    report_string = json.dumps(report, sort_keys=True)
    return hashlib.sha256(report_string.encode()).hexdigest()


if __name__ == "__main__":
    sample_report = {
        "user_id": "U001",
        "risk_score": 0.82,
        "risk_level": "High",
        "model_version": "v1.0"
    }

    report_hash = generate_hash(sample_report)
    print("Generated Hash:", report_hash)
