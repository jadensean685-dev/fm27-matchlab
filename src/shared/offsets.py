"""Memory offsets for FM27 builds — community maintained, PRs welcome."""

OFFSETS = {
    "build_27_1_0": {
        "transfer_budget": 0x1A4C3F0,
        "ca_pa_block": 0x2B11E20,
        "injury_flags": 0x1A4C428,
    },
    "build_27_1_1": {
        "transfer_budget": 0x1A4D110,
        "ca_pa_block": 0x2B12F40,
        "injury_flags": 0x1A4D148,
    },
}


def for_build(build: str) -> dict[str, int]:
    return OFFSETS.get(build, {})