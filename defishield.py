
import math


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

    if case["max_oracle_age_seconds"] <= 0:
        return {
            "verdict": "INCONCLUSIVE",
            "reason": "Maximum oracle age must be greater than zero."
        }

    if case["oracle_age_seconds"] > case["max_oracle_age_seconds"]:
        return {
            "verdict": "SUPPORTED",
            "reason": "Oracle data exceeds the configured maximum age."
        }

    if (
        case["price_deviation_percent"]
        > case["max_price_deviation_percent"]
    ):
        return {
            "verdict": "SUPPORTED",
            "reason": "Price deviation exceeds the configured tolerance."
        }

    if case["collateral_ratio"] <= case["liquidation_threshold"]:
        return {
            "verdict": "CONTRADICTED",
            "reason": (
                "The supplied figures meet the configured liquidation condition."
            )
        }

    return {
        "verdict": "SUPPORTED",
        "reason": (
            "The supplied figures do not meet the configured liquidation condition."
        )
    }
