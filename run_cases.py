
import json
from datetime import datetime, timezone
from pathlib import Path

from defishield import evaluate_dispute


def main():
    cases_file = Path(__file__).parent / "data" / "sample_cases.json"

    with cases_file.open("r", encoding="utf-8") as file:
        cases = json.load(file)

    print("DeFiShield Liquidation Dispute Evaluator")
    print("Checked at:", datetime.now(timezone.utc).isoformat())
    print("Total cases:", len(cases))
    print("-" * 50)

    for case in cases:
        result = evaluate_dispute(case)

        case_id = case.get("case_id", case.get("id", "Unknown case"))

        print("Case:", case_id)
        print("Verdict:", result["verdict"])
        print("Reason:", result["reason"])
        print("-" * 50)


if __name__ == "__main__":
    main()
