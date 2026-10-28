
# DeFiShield

A GenLayer-based prototype for investigating DeFi liquidation disputes.

## Problem

Liquidation disputes can arise when a borrower believes a liquidation used
an incorrect, stale, or otherwise questionable price.

## Proposed Solution

DeFiShield evaluates a submitted liquidation case against available evidence
and documented protocol rules.

## Planned Verdicts

- SUPPORTED: Evidence supports the liquidation dispute.
- CONTRADICTED: Evidence conflicts with the dispute.
- INCONCLUSIVE: Evidence is insufficient to reach a reliable conclusion.

## Project Scope

- Historical and simulated cases only
- Evidence-based adjudication
- Transparent verdicts and explanations
- Automated tests for conflicting or missing evidence

## Safety

This is an experimental prototype. It does not control funds, execute trades,
or provide authoritative financial or legal decisions.

## Status

Initial setup. Development has not yet begun.
