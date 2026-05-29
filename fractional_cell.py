from __future__ import annotations
from dataclasses import dataclass


@dataclass
class FractionalCell:
    value: float = 0.0

    def add(self, other):
        return FractionalCell(self.value + other.value)

    def sub(self, other):
        return FractionalCell(self.value - other.value)

    def mul(self, other):
        return FractionalCell(self.value * other.value)

    def div(self, other):
        if other.value == 0:
            raise ZeroDivisionError()
        return FractionalCell(self.value / other.value)

    def __repr__(self):
        return f"{self.value:.6f}"
