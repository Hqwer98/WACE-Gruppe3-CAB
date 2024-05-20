import numpy as np
import matplotlib.pyplot as plt
from Derivative import Derivative


def f(x):
    return 0.2 * np.power(x, 3) + x


x = np.linspace(-4, 4, 100)
f0 = f(x)
h = 0.01

f1 = Derivative.of_order_1(f, x, h)

plt.plot(x, f0, label='f(x)')
plt.plot(x, f1, label='f´(x)')
plt.legend()
plt.title('Erste Ableitung der Funktion f')
plt.grid()
plt.show()