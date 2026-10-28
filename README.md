# DeFiShield

A prototype for investigating DeFi liquidation disputes using Python and GenLayer intelligent contracts.

## Problem

Liquidation disputes can arise when a borrower believes a liquidation was triggered using stale oracle data, incorrect prices, or incorrectly applied protocol rules.

## Proposed Solution

DeFiShield evaluates liquidation cases against configurable rules and submitted evidence, producing a verdict with an explanation.

## Verdicts

- **SUPPORTED:** The configured rules identify evidence supporting the dispute.
- **CONTRADICTED:** The configured rules indicate that the stated liquidation condition was met.
- **INCONCLUSIVE:** The evidence is invalid or insufficient to reach a verdict.

## Current Features

- Python-based evaluation prototype
- Collateral ratio and liquidation threshold checks
- Oracle data age validation
- Price deviation validation
- Input validation
- Sample cases and automated unit tests
- GenLayer intelligent contract prototype

## Project Structure

- `defishield.py`: Python evaluator
- `run_cases.py`: Runs sample cases
- `data/sample_cases.json`: Sample case data
- `tests/`: Automated Python tests
- `contracts/defishield.py`: GenLayer contract
- `frontend/`: Frontend development folder

## Safety and Limitations

This is an experimental prototype using simplified demonstration rules. It does not control funds, execute trades, or provide authoritative financial or legal decisions. Results depend on the configured rules and the quality of the submitted evidence.

## Future Improvements

- Integrate verifiable historical transaction evidence
- Add protocol-specific liquidation rules
- Validate oracle prices and timestamps against reliable sources
- Expand contract testing
- Build a frontend for submitting and reviewing disputes