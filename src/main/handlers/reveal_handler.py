"""Attribute reveal — dumps hidden player CA/PA values for local analysis."""
import json
from pathlib import Path


class RevealHandler:
    def __init__(self, engine: object) -> None:
        self.engine = engine
        self.out = Path.home() / "Documents" / "fm27-matchlab" / "reveal.json"

    def dump_attributes(self) -> Path:
        self.out.parent.mkdir(parents=True, exist_ok=True)
        payload = {"note": "stub — wire to scanner offsets in offsets.py", "players": []}
        self.out.write_text(json.dumps(payload, indent=2), encoding="utf-8")
        return self.out