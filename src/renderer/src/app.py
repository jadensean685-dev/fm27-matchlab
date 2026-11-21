"""Renderer root window — cheat control panel for FM27 MatchLab."""
from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout

from src.renderer.src.components.cheat_panel import CheatPanel


class MatchLabWindow(QMainWindow):
    def __init__(self, bridge) -> None:
        super().__init__()
        self.bridge = bridge
        self.setWindowTitle("FM27 MatchLab — Cheats")
        self.resize(720, 520)
        root = QWidget()
        layout = QVBoxLayout(root)
        layout.addWidget(CheatPanel(bridge))
        self.setCentralWidget(root)