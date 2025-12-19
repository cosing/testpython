from dataclasses import dataclass as _dataclass


@_dataclass
class User:
    name: str

    def printname(self):
        print(self.name)
