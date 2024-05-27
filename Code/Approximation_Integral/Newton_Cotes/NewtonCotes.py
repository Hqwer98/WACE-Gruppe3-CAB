from typing import Callable
import numpy as np


class NewtonCotes:
    """
    Used for approximation of the Integral.
    The weightOptions attribute is a list of numpy-arrays with the different variants of the newton cotes formulas.
    It is dependent on the amount of the nodes that are used.
    """
    weightOptions = [
        np.array([1, 1]) * 1 / 2,  #trapezoidal rule
        np.array([1, 4, 1]) * 1 / 3,  #simpson rule
        np.array([1, 3, 3, 1]) * 3 / 8,  #3/8 rule
        np.array([7, 32, 12, 32, 7]) * 2 / 45,  #milne rule
    ]

    def __init__(self, n: int):
        """
        Creates an instance of the NewtonCotes class for the approximation of the integral.
        :param n: number of nodes for the approximation of the integral from 1 to 4
        """
        assert 0 < n < 5 and isinstance(n, int)
        self.n = n
        self.weight = self.weightOptions[n - 1]

    def calculate_integral(self, f: Callable[[float], float], a: float, b: float) -> float:
        """
        Calculates the Integral of a function with respect to the weightOptions attribute and the given n
        :param f: function f(x)
        :param a: lower bound of the integral
        :param b: upper bound of the integral
        :return: the approximated integral of the function
        """
        A = 0
        h = (b - a) / self.n
        for i in range(self.n + 1):
            xi = a + i * h
            A += self.weight[i] * f(xi)
        A *= h
        return A
