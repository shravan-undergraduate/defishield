
import math
from datetime import datetime, timezone


REQUIRED_FIELDS = [
    "collateral_ratio",
    "liquidation_threshold",
    "oracle_age_seconds",
    "max_oracle_age_seconds",
    "price_deviation_percent",
    "max_price_deviation_percent",
]


def evaluate_dispute(case):
    if not isinstance(case, dict):
        return {
            "verdict": "INCONCLUSIVE",
            "reason": "Case data must be a dictionary."
        }

    for field in REQUIRED_FIELDS:
        if field not in case or case[field] is None:
            return {
                "verdict": "INCONCLUSIVE",
                "reason": f"Required evidence is missing: {field}."
            }

        value = case[field]

        if (
            isinstance(value, bool)
            or not isinstance(value, (int, float))
            or not math.isfinite(value)
            or value < 0
        ):
            return {
                "verdict": "INCONCLUSIVE",
                "reason": f"Invalid evidence value: {field}."
            }

    if case["oracle_age_seconds"] > case["max_oracle_age_seconds"]:
        return {
            "verdict": "SUPPORTED",
            "reason": "Oracle data exceeds the configured maximum age."
        }

    if case["price_deviation_percent"] > case["max_price_deviation_percent"]:
        return {
            "verdict": "SUPPORTED",
            "reason": "Price deviation exceeds the configured tolerance."
        }

    if case["collateral_ratio"] <= case["liquidation_threshold"]:
        return {
            "verdict": "CONTRADICTED",
            "reason": "The supplied figures meet the configured liquidation condition."
        }

    return {
        "verdict": "SUPPORTED",
        "reason": "The supplied figures do not meet the configured liquidation condition."
    }


def main():
    example_case = {
        "collateral_ratio": 1.35,
        "liquidation_threshold": 1.50,
        "oracle_age_seconds": 180,
        "max_oracle_age_seconds": 60,
        "price_deviation_percent": 1.0,
        "max_price_deviation_percent": 2.0,
    }

    result = evaluate_dispute(example_case)

    print("DeFiShield Liquidation Dispute Evaluator")
    print("Checked at:", datetime.now(timezone.utc).isoformat())
    print("Verdict:", result["verdict"])
    print("Reason:", result["reason"])


    def test_invalid_text_value(self):
        self.case["oracle_age_seconds"] = "old"

        result = evaluate_dispute(self.case)

        self.assertEqual(result["verdict"], "INCONCLUSIVE")

    def test_missing_required_field(self):
        del self.case["liquidation_threshold"]

        result = evaluate_dispute(self.case)

        self.assertEqual(result["verdict"], "INCONCLUSIVE")

if __name__ == "__main__":
    main()
