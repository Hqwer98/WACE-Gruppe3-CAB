from typing import Callable
import numpy as np


class NewtonCotes:
    weightOptions = [
        np.array([1, 1]) * 1 / 2,  #trapezoidal rule
        np.array([1, 4, 1]) * 1 / 3,  #simpson rule
        np.array([1, 3, 3, 1]) * 3 / 8,  #3/8 rule
        np.array([7, 32, 12, 32, 7]) * 2 / 45,  #milne rule
    ]

    def __init__(self, n: int):
        assert n > 0 and isinstance(n, int)
        self.n = n
        self.weight = self.weightOptions[n - 1]

    def calculate_integral(self, f: Callable[[float], float], a: float, b: float) -> float:
        A = 0
        h = (b - a) / self.n
        for i in range(self.n + 1):
            xi = a + i * h
            A += self.weight[i] * f(xi)
        A *= h
        return A
