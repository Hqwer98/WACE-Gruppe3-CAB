import numpy as np
import sympy as sp
import matplotlib as plt

test = 123
print(test)

print("Hello World!")
print("moin moin meister nase")

print("Test-C")


def apply(x):
    return x / 1


def f(x):
    return np.square(x) + 1


x = sp.Symbol('x')
f = x ** 2 + 1

f_numeric = sp.lambdify(x, f, 'numpy')

x_values = np.linspace(-5, 5, 100)
f_values = f_numeric(x_values)

f_ableitung_ganz = np.gradient(f_values, x_values)

print("Ganze-Ableitung von f(x):", f_ableitung_ganz)

# matplotlib

x = np.array(-3, 3, 0.01)
y = f(x)
plt.plot(x, y)
plt.show()
