
from datetime import datetime, timezone


def evaluate_dispute(case):
    required_fields = [
        "collateral_ratio",
        "liquidation_threshold",
        "oracle_age_seconds",
        "max_oracle_age_seconds",
        "price_deviation_percent",
        "max_price_deviation_percent",
    ]

    if any(field not in case or case[field] is None for field in required_fields):
        return {
            "verdict": "INCONCLUSIVE",
            "reason": "Required evidence is missing."
        }

    if any(case[field] < 0 for field in [
        "collateral_ratio",
        "liquidation_threshold",
        "oracle_age_seconds",
        "max_oracle_age_seconds",
        "price_deviation_percent",
        "max_price_deviation_percent",
    ]):
        return {
            "verdict": "INCONCLUSIVE",
            "reason": "Evidence contains invalid negative values."
        }

    if case["oracle_age_seconds"] > case["max_oracle_age_seconds"]:
        return {
            "verdict": "SUPPORTED",
            "reason": "The recorded oracle price exceeded the allowed age."
        }

    if case["price_deviation_percent"] > case["max_price_deviation_percent"]:
        return {
            "verdict": "SUPPORTED",
            "reason": "The recorded price differed beyond the configured tolerance."
        }

    if case["collateral_ratio"] <= case["liquidation_threshold"]:
        return {
            "verdict": "CONTRADICTED",
            "reason": "The supplied figures indicate the position met the liquidation condition."
        }

    return {
        "verdict": "SUPPORTED",
        "reason": "The supplied figures do not indicate that the position met the liquidation condition."
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


if __name__ == "__main__":
    main()
