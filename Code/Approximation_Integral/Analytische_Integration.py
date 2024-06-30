import matplotlib.pyplot as plt
import numpy as np

from Code.Approximation_Integral.Newton_Cotes.NewtonCotes import NewtonCotes

a = 0
b = 3

def f(x):
    return np.square(x)

newtonCotes = NewtonCotes(2)

x = np.linspace(a, b, 100)
y = f(x)

plt.figure(figsize=(5, 5))
plt.plot(x, y, label=r'$x^2$')
plt.title(r' Funktion $x^2$')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()

area = newtonCotes.calculate_integral(f, a, b)

plt.fill_between(x, y, color='blue', alpha=0.2, label=r'$\int_{a}^{b}x^2dx = $' + str(area))
plt.legend(loc='upper left')

plt.show()
