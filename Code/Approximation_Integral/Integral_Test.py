import numpy as np
import matplotlib.pyplot as plt
from Code.Approximation_Integral.Newton_Cotes.NewtonCotes import NewtonCotes
from Code.Approximation_Integral.Newton_Cotes.TrapezoidalRule import TrapezoidalRule
from Code.Approximation_Integral.Newton_Cotes.SimpsonRule import SimpsonRule


def f(x):
    return 4 * np.power(x, 3) + 2 * x


def g(x):
    return np.sin(x)


trapezoidalRule = TrapezoidalRule()
simpsonRule = SimpsonRule()
rule1 = NewtonCotes(3)
rule2 = NewtonCotes(4)

print(trapezoidalRule.calculate_integral(f, 1, np.pi))
print("-----------")
print(trapezoidalRule.calculate_integral_composite(f, 1, np.pi))
print("-----------")
print(simpsonRule.calculate_integral(f, 1, np.pi))
print("-----------")
print(simpsonRule.calculate_integral_simple(f, 1, np.pi))
print("-----------")
print(simpsonRule.calculate_integral_composite(f, 1, np.pi))
print("-----------")
print(rule1.calculate_integral(f, 1, np.pi))
print("-----------")
print(rule2.calculate_integral(f, 1, np.pi))
