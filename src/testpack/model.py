from dataclasses import dataclass as _dataclass
from typing import Self


@_dataclass
class User:
    name: str
    age: int
    money: int = 0

    def printname(self):
        print(self.name)

    def print_age_stage(self):
        if self.age <= 0:
            print("Illegal age")
        elif self.age < 18:
            print("Minor")
        elif self.age < 60:
            print("Adult")
        else:
            print("Elderly")

    def add_money(self, i: int):
        self.money += i

    def pay_to(self, other_user: Self, amount: int):
        if self.money >= amount:
            self.add_money(-amount)
            other_user.add_money(amount)
            print(f"{self.name} paid {amount} to {other_user.name}.")
        else:
            # 补全错误类型，并提供清晰的错误信息
            raise ValueError(
                f"{self.name} has insufficient funds (Balance: {self.money})"
            )
