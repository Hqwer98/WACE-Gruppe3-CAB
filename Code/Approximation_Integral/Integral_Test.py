from typing import Callable

import numpy as np
import matplotlib.pyplot as plt
from Code.Approximation_Integral.Newton_Cotes.NewtonCotes import NewtonCotes
from Code.Approximation_Integral.Newton_Cotes.TrapezoidalRule import TrapezoidalRule
from Code.Approximation_Integral.Newton_Cotes.SimpsonRule import SimpsonRule


def f(x):
    return 4 * np.power(x, 3) + 2 * x


def g(x):
    return np.sin(x)


def test_approximation(function: Callable, a: float, b: float):
    trapezoidalRule = TrapezoidalRule()
    simpsonRule = SimpsonRule()
    rule1 = NewtonCotes(3)
    rule2 = NewtonCotes(4)

    trapezoidal_composite_result = trapezoidalRule.calculate_integral_composite(function, a, b)
    simpson_simple_result = simpsonRule.calculate_integral_simple(function, a, b)
    newton_cotes_result1 = rule1.calculate_integral(function, a, b)
    newton_cotes_result2 = rule2.calculate_integral(function, a, b)

    print("Trapez-Regel Ergebnis:", trapezoidal_composite_result)
    print("Simpson-Regel Ergebnis:", simpson_simple_result)
    print("3/8-Regel Ergebnis:", newton_cotes_result1)
    print("Milne-Regel Ergebnis:", newton_cotes_result2)


def plot_function_with_integral(function: Callable, a: float, b: float, node_count=4):
    x = np.linspace(a, b, 1000)
    y = function(x)

    plt.figure(figsize=(12, 6))
    plt.plot(x, y, label=r'$f(x) = 4x^3 + 2x$')

    plt.title('Funktion und das tatsächliche Integral')
    plt.fill_between(x, y, color='blue', alpha=0.2, label=r'$\int_0^1 f(x) dx = 2$')
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(linestyle="--")
    plt.show()

    simpsonRule = SimpsonRule(node_count)
    y = simpsonRule.get_plotting_values(function, a, b)
    x = np.linspace(a, b, len(y))

    plt.figure(figsize=(12, 6))
    plt.plot(x, y, label=r'$f(x) = 4x^3 + 2x$')
    plt.title('Funktion und das approximierte Integral (Simpson mit ' + str(node_count) + ' Knoten)')
    plt.fill_between(x, y, color='green', alpha=0.2, label=r'$\int_0^1 f(x) dx \approx 2$')
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(linestyle="--")
    plt.show()


plot_function_with_integral(f, 0, 1)
test_approximation(g, 0, np.pi)
