from __future__ import annotations
import math
from fractional_cell import FractionalCell


class ComplexCell:

    def __init__(self, real=0.0, imag=0.0):
        self.real = FractionalCell(real)
        self.imag = FractionalCell(imag)

    def add(self, other):
        return ComplexCell(
            self.real.value + other.real.value,
            self.imag.value + other.imag.value
        )

    def sub(self, other):
        return ComplexCell(
            self.real.value - other.real.value,
            self.imag.value - other.imag.value
        )

    def mul(self, other):
        a, b = self.real.value, self.imag.value
        c, d = other.real.value, other.imag.value
        return ComplexCell((a*c) - (b*d), (a*d) + (b*c))

    def div(self, other):
        a, b = self.real.value, self.imag.value
        c, d = other.real.value, other.imag.value
        denom = c*c + d*d
        if denom == 0:
            raise ZeroDivisionError()
        return ComplexCell((a*c + b*d) / denom, (b*c - a*d) / denom)

    def magnitude(self):
        return math.sqrt(self.real.value**2 + self.imag.value**2)

    def __repr__(self):
        r, i = self.real.value, self.imag.value
        if i >= 0:
            return f"{r:.6f}+{i:.6f}i"
        return f"{r:.6f}{i:.6f}i"
