from src.main.handlers.trainer_handler import TrainerHandler


def test_toggle_flips():
    h = TrainerHandler(engine=object())
    assert h.toggle("no_injuries") is True
    assert h.toggle("no_injuries") is False