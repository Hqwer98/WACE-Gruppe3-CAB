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


def test_approximation(
        function: Callable[[np.ndarray], np.ndarray],
        expected_derivative_order_1: np.ndarray,
        expected_derivative_order_2: np.ndarray,
        grace_value: float
) -> bool:
    """
    Tests for x = [0, 1, 2, 3, 4] if the first and second Derivative is approximately
    calculated correctly with the values of the given function
    :param function: Function to be tested
    :param expected_derivative_order_1: Expected values of the first derivative
    :param expected_derivative_order_2: Expected values of the second derivative
    :param grace_value: a value that indicates the maximum deviation
    :return: False if the grace value is smaller than the difference, otherwise True
    """
    if len(expected_derivative_order_1) != 5 or len(expected_derivative_order_2) != 5:
        raise ValueError("Please choose an expected array with 5 elements")

    test_x = np.array([0, 1, 2, 3, 4])
    value_range = len(test_x)
    test_derivative_order_1 = Derivative.of_order_1(function, test_x, grace_value)
    test_derivative_order_2 = Derivative.of_order_2(function, test_x, grace_value)

    for i in range(value_range):
        if grace_value < abs(expected_derivative_order_1[i] - test_derivative_order_1[i]):
            return False
        if grace_value < abs(expected_derivative_order_2[i] - test_derivative_order_2[i]):
            return False

    not_expected_derivate_order_1 = expected_derivative_order_1 + 2 * grace_value
    not_expected_derivate_order_2 = expected_derivative_order_2 + 2 * grace_value
    for i in range(value_range):
        if grace_value > abs(not_expected_derivate_order_1[i] - test_derivative_order_1[i]):
            return False
        if grace_value > abs(not_expected_derivate_order_2[i] - test_derivative_order_2[i]):
            return False
    return True


expectation_of_first_derivative = np.array([0, 4, 8, 12, 16])
expectation_of_second_derivative = np.array([4, 4, 4, 4, 4])
print(test_approximation(g, expectation_of_first_derivative, expectation_of_second_derivative, 0.01))


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
