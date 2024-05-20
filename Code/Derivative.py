import numpy as np


class Derivative:
    @staticmethod
    def of_order_1(f, x, h):
        """
        Calculates the first derivative of f with respect to x
        :param f: function f(x)
        :param x: x value
        :param h: approximation value around x
        :return: the approximate derivative of f with respect to x
        """
        return (f(x + h) - f(x - h)) / (2 * h)

    @staticmethod
    def of_order_2(f, x, h):
        """
        Calculates the second derivative of f with respect to x
        :param f: function f(x)
        :param x: x value
        :param h: approximation value around x
        :return: the approximate second derivative of f with respect to x
        """
        return (f(x + h) - 2 * f(x) - f(x - h)) / (np.square(h))
