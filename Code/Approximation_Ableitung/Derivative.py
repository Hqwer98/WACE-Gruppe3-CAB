import numpy as np
from typing import Callable


class Derivative:
    """
    Derivative class to calculate the derivative of a function
    """
    @staticmethod
    def of_order_1(f: Callable[[np.ndarray], np.ndarray], x: np.ndarray, h: float) -> np.ndarray:
        """
        Calculates the first derivative of f with respect to x
        :param f: function f(x)
        :param x: x value
        :param h: approximation value around x
        :return: the approximate derivative of f with respect to x
        """
        assert h != 0
        return (f(x + h) - f(x - h)) / (2 * h)

    @staticmethod
    def of_order_2(f: Callable[[np.ndarray], np.ndarray], x: np.ndarray, h: float) -> np.ndarray:
        """
        Calculates the second derivative of f with respect to x
        :param f: function f(x)
        :param x: x value
        :param h: approximation value around x
        :return: the approximate second derivative of f with respect to x
        """
        assert h != 0
        return (f(x + h) - 2 * f(x) + f(x - h)) / (h * h)
