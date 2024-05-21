import numpy as np
import matplotlib.pyplot as plt
from Derivative import Derivative
from typing import Callable


def f(x: np.ndarray) -> np.ndarray:
    """
    Defines function f
    :param x: x value
    :return: the function (1/27)*x^3
    """
    return 1 / 27 * np.power(x, 3)


def plot_function_with_derivatives(function: Callable[[np.ndarray], np.ndarray], i: float, function_expression: str):
    x = np.linspace(-i, i, 100)
    f = function(x)
    h = 0.01

    df = Derivative.of_order_1(function, x, h)
    ddf = Derivative.of_order_2(function, x, h)

    plt.plot(x, f, label=r'$f(x)$')
    plt.plot(x, df, label=r'$f´(x)$')
    plt.plot(x, ddf, label=r'$f´´(x)$')
    plt.legend()
    plt.title('Funktion ' + function_expression + ' mit erste und zweite Ableitung')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()
    plt.show()


plot_function_with_derivatives(f, 4, r'f(x) = $\frac{1}{27}x^3$')
