"""Cheat panel — toggles for trainer, reveal, and budget modules."""
from PySide6.QtWidgets import QCheckBox, QPushButton, QVBoxLayout, QWidget


class CheatPanel(QWidget):
    def __init__(self, bridge) -> None:
        super().__init__()
        self.bridge = bridge
        layout = QVBoxLayout(self)
        for cheat_id, label in [
            ("no_injuries", "No Injuries"),
            ("infinite_budget", "Infinite Transfer Budget"),
            ("reveal_ca_pa", "Reveal CA / PA"),
            ("match_fix", "Match Fix (win)"),
        ]:
            box = QCheckBox(label)
            box.toggled.connect(lambda on, cid=cheat_id: self._toggle(cid, on))
            layout.addWidget(box)
        reveal_btn = QPushButton("Dump Attributes")
        reveal_btn.clicked.connect(self.bridge.reveal_attributes)
        layout.addWidget(reveal_btn)

    def _toggle(self, cheat_id: str, on: bool) -> None:
        self.bridge.toggle_trainer(cheat_id)