
import json
from pathlib import Path

from defishield import evaluate_dispute


def main():
    data_file = Path(__file__).parent / "data" / "sample_cases.json"

    with data_file.open("r", encoding="utf-8") as file:
        cases = json.load(file)

    for case in cases:
        result = evaluate_dispute(case)

        print(f"\nCase: {case['case_id']}")
        print(f"Description: {case['description']}")
        print(f"Verdict: {result['verdict']}")
        print(f"Reason: {result['reason']}")


if __name__ == "__main__":
    main()
