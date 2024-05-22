import numpy as np
import matplotlib.pyplot as plt
from Trapezregel.TrazezoidalRule import TrapezoidalRule


def f(x):
    return np.sin(x)


trapezoidalRule = TrapezoidalRule()

print(trapezoidalRule.calculate_integral(f, 0, np.pi))
