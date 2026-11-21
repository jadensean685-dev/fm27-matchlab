"""Transfer budget cheat module (single-player sandbox only)."""
from dataclasses import dataclass


@dataclass
class TransferBudgetCheat:
    cheat_id: str = "transfer_budget"
    target_value: int = 500_000_000

    def apply(self, snapshot: dict) -> dict:
        snapshot = dict(snapshot)
        snapshot["transfer_budget"] = self.target_value
        return snapshot