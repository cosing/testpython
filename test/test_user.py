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

@pytest.mark.parametrize(
    "money_init, money_trans, should_fail",
    [
        (100, 50, False),   # 正常支付
        (100, 100, False),  # 刚好付清（边界值）
        (100, 150, True),   # 余额不足（预期报错）
        (0, 1, True),       # 零余额支付（预期报错）
    ],
)
def test_money_transform(money_init: int, money_trans: int, should_fail: bool):
    u0 = User(name="Jone", age=18)
    u1 = User(name="Alice", age=18)
    u0.add_money(money_init)

    if should_fail:
        # 使用 pytest.raises 捕获预期的异常
        with pytest.raises(ValueError) as excinfo:
            u0.pay_to(u1, money_trans)
        # 还可以断言错误信息是否符合预期
        assert "insufficient funds" in str(excinfo.value)
    else:
        u0.pay_to(u1, money_trans)
        assert u0.money == money_init - money_trans
        assert u1.money == money_trans