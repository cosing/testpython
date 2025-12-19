import logging
from testpack.model import User
import pytest


def test_user_creation():
    """Tests if a User object can be created with the correct name."""
    user = User(name="testuser", age=18)
    assert user.name == "testuser"


def test_print_name(capsys: pytest.CaptureFixture[str]):
    """Tests if the printname method prints the correct name to stdout."""
    user = User(name="testuser", age=18)
    user.printname()
    captured = capsys.readouterr()
    assert captured.out == "testuser\n"


def test_random_name(random_str: str):
    """Tests if the printname method prints the correct name to stdout."""
    user = User(name=random_str, age=18)
    user.printname()
    logging.info(f"{user.name}")
    assert user.name == random_str


@pytest.mark.parametrize(
    "age, expected_print",
    [
        (-1, "Illegal age\n"),
        (0, "Illegal age\n"),
        (17, "Minor\n"),
        (18, "Adult\n"),
        (60, "Elderly\n"),
        (100, "Elderly\n"),
    ],
)
def test_age_stages(capsys: pytest.CaptureFixture[str], age: int, expected_print: str):
    user = User(name="Jone", age=age)
    user.print_age_stage()
    captured = capsys.readouterr()
    assert captured.out == expected_print
