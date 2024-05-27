from typing import Callable
from Code.Approximation_Integral.Newton_Cotes.NewtonCotes import NewtonCotes


class SimpsonRule(NewtonCotes):
    """
    Used for approximation of the integral.
    This class is a child of the NewtonCotes class and represents the more accurate version of the Simpson rule.
    It uses the simpson rule with a higher amount of nodes but the weights stay the same.
    """
    def __init__(self, node_count=10):
        """
        Creates an instance of the SimpsonRule class.
        The node count has to be even for the simpson rule to work.
        :param node_count: number of nodes to approximate an integral
        """
        super().__init__(2)
        assert node_count > 0
        assert node_count % 2 == 0
        self.node_count = node_count

    def calculate_integral_composite(self, f: Callable[[float], float], a: float, b: float) -> float:
        """
        Calculates the integral of a function with the simpson rule in regard to the given nodes.
        :param f: function f(x)
        :param a: lower bound of the integral
        :param b: upper bound of the integral
        :return: the approximated integral of the function
        """
        h = (b - a) / self.node_count
        A = f(a) + f(b)
        for i in range(1, self.node_count):
            xi = a + i * h
            if i % 2 == 0:
                A += 2 * f(xi)
            else:
                A += 4 * f(xi)
        return A * h / 3

    def calculate_integral_simple(self, f: Callable[[float], float], a: float, b: float) -> float:
        """
        Calculates the integral of a function with the simpson rule with the minimal amount of nodes.
        :param f: function f(x)
        :param a: lower bound of the integral
        :param b: upper bound of the integral
        :return: the approximated integral of the function
        """
        h = (b - a) / 6
        return h * (f(a) + f(b) + 4 * f((a + b)/2))
