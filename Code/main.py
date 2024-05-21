import numpy as np
import matplotlib.pyplot as plt
from Derivative import Derivative
from typing import Callable


def f(x: np.ndarray) -> np.ndarray:
    return 1 / 27 * np.power(x, 3)


def g(x: np.ndarray) -> np.ndarray:
    return 2 * np.square(x) + 1


def h(x: np.ndarray) -> np.ndarray:
    return np.sin(x / np.pi)


def plot_function_with_derivatives(function: Callable[[np.ndarray], np.ndarray], i: float, function_name: str,
                                   function_expression: str):
    """
    Plots function f and its derivatives
    :param function: function to be plotted
    :param i: interval to plot
    :param function_name: name of the function
    :param function_expression: mathematical expression of the function
    """
    x = np.linspace(-i, i, 100)
    f = function(x)
    h = 0.01

    df = Derivative.of_order_1(function, x, h)
    ddf = Derivative.of_order_2(function, x, h)

    plt.plot(x, f, label=r'$f(x)$')
    plt.plot(x, df, label=r'$f´(x)$')
    plt.plot(x, ddf, label=r'$f´´(x)$')
    plt.legend(loc='lower right')
    plt.title('Funktion ' + function_name + ' = ' + function_expression + ' mit erste und zweite Ableitung')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()
    plt.show()


plot_function_with_derivatives(f, 4, 'f(x)', r'$\frac{1}{27}x^3$')
plot_function_with_derivatives(g, 4, 'g(x)', r'$2x^2 + 1$')
plot_function_with_derivatives(h, 4 * np.pi, 'h(x)', r'$sin(\frac{x}{\pi})$')
