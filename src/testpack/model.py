from dataclasses import dataclass as _dataclass


@_dataclass
class User:
    name: str
    age: int

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
