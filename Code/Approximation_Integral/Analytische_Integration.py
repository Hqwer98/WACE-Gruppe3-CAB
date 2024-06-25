import matplotlib.pyplot as plt
import numpy as np

from Code.Approximation_Integral.Newton_Cotes.SimpsonRule import SimpsonRule

def f(x):
    return x**2

newtonCotes = SimpsonRule()

a = 0
b = 10

x = np.linspace(a, b, 100)
y = (1/3) * x**3

plt.figure(figsize=(5, 5))
plt.plot(x, y, label=r'$\frac{1}{3}x^3$')
plt.title(r' Funktion $\frac{1}{3}x^3$')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.legend(loc='upper left')

x = np.linspace(a, b, 100)
y = newtonCotes.get_plotting_values(f,a,b)

plt.figure(figsize=(5,5))
plt.plot(x, y, label=r'$\frac{1}{3}x^3$')
plt.title(r' Funktion $\frac{1}{3}x^3$')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.legend(loc='upper left')

plt.show()

