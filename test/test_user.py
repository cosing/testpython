import logging
from testpack.model import User
import pytest


def test_user_creation():
    """Tests if a User object can be created with the correct name."""
    user = User(name="testuser")
    assert user.name == "testuser"


def test_printname(capsys: pytest.CaptureFixture[str]):
    """Tests if the printname method prints the correct name to stdout."""
    user = User(name="testuser")
    user.printname()
    captured = capsys.readouterr()
    assert captured.out == "testuser\n"


def test_randname(random_str: str):
    """Tests if the printname method prints the correct name to stdout."""
    user = User(name=random_str)
    user.printname()
    logging.info(f"{user.name}")
    assert user.name == random_str
