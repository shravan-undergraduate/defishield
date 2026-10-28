#{ "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }

from genlayer import *


class DeFiShield(gl.Contract):

    def __init__(self):
        pass

    @gl.public.view
    def evaluate_case(
        self,
        collateral_ratio: i32,
        liquidation_threshold: i32,
        oracle_age_seconds: i32,
        max_oracle_age_seconds: i32,
        price_deviation_bps: i32,
        max_price_deviation_bps: i32,
    ) -> str:

        if (
                   if (
            collateral_ratio < 0
            or liquidation_threshold < 0
            or oracle_age_seconds < 0
            or max_oracle_age_seconds <= 0
            or price_deviation_bps < 0
            or max_price_deviation_bps < 0
        ):
            return "INCONCLUSIVE: Invalid input or configuration."
        ):
            return "INCONCLUSIVE: Invalid negative input."

        if oracle_age_seconds > max_oracle_age_seconds:
            return "SUPPORTED: Oracle data exceeds the configured age limit."

        if price_deviation_bps > max_price_deviation_bps:
            return "SUPPORTED: Price deviation exceeds the configured limit."

        if collateral_ratio <= liquidation_threshold:
            return "CONTRADICTED: Position meets the configured liquidation condition."

        return "SUPPORTED: Position is above the configured liquidation threshold."
