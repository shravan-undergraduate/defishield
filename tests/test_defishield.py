
import unittest

from defishield import evaluate_dispute


class TestDeFiShield(unittest.TestCase):

    def setUp(self):
        self.case = {
            "collateral_ratio": 1.35,
            "liquidation_threshold": 1.50,
            "oracle_age_seconds": 30,
            "max_oracle_age_seconds": 60,
            "price_deviation_percent": 1.0,
            "max_price_deviation_percent": 2.0,
        }

    def test_stale_oracle_price(self):
        self.case["oracle_age_seconds"] = 180

        result = evaluate_dispute(self.case)

        self.assertEqual(result["verdict"], "SUPPORTED")

    def test_liquidation_condition_was_met(self):
        self.case["collateral_ratio"] = 1.40

        result = evaluate_dispute(self.case)

        self.assertEqual(result["verdict"], "CONTRADICTED")

    def test_missing_evidence(self):
        self.case["price_deviation_percent"] = None

        result = evaluate_dispute(self.case)

        self.assertEqual(result["verdict"], "INCONCLUSIVE")

    def test_excessive_price_deviation(self):
        self.case["price_deviation_percent"] = 5.0

        result = evaluate_dispute(self.case)

        self.assertEqual(result["verdict"], "SUPPORTED")

    def test_negative_evidence_value(self):
        self.case["oracle_age_seconds"] = -10

        result = evaluate_dispute(self.case)

        self.assertEqual(result["verdict"], "INCONCLUSIVE")


if __name__ == "__main__":
    unittest.main()
