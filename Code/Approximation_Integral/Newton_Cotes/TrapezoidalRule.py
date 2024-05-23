import numpy as np
from typing import Callable
from Code.Approximation_Integral.Newton_Cotes.NewtonCotes import NewtonCotes


class TrapezoidalRule(NewtonCotes):
    def __init__(self, node_count=10):
        super().__init__(1)
        self.node_count = node_count

    def calculate_integral(self, f: Callable[[float], float], a: float, b: float) -> float:
        h = (b - a) / self.node_count
        A = self.weight[0] * f(a) + self.weight[1] * f(b)
        for i in range(1, self.node_count):
            xi = a + i * h
            A += f(xi)
        return A * h
