import numpy as np
from typing import Callable
from Code.Approximation_Integral.Newton_Cotes.NewtonCotes import NewtonCotes


class TrapezoidalRule(NewtonCotes):
    """
    Used for approximation of the integral.
    This class is a child of the NewtonCotes class and represents the more accurate version of the Trapezoidal rule.
    It uses the trapezoidal rule with a higher amount of nodes but the weights stay the same.
    """
    def __init__(self, node_count=10):
        """
        Creates an instance of the TrapezoidalRule class.
        :param node_count: number of nodes to approximate an integral
        """
        super().__init__(1)
        assert node_count > 0
        self.node_count = node_count

    def calculate_integral(self, f: Callable[[float], float], a: float, b: float) -> float:
        """
        Calculates the integral of a function with the trapezoidal rule in regard to the given nodes.
        :param f: function f(x)
        :param a: lower bound of the integral
        :param b: upper bound of the integral
        :return: the approximated integral of the function
        """
        h = (b - a) / self.node_count
        A = self.weight[0] * f(a) + self.weight[1] * f(b)
        for i in range(1, self.node_count):
            xi = a + i * h
            A += f(xi)
        return A * h
