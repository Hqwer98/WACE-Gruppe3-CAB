import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

test = 123
print(test)

print("Hello World!")
print("moin moin meister nase")

print("Test-C")


def apply(x):
    return x / 1


def f(x):
    return np.square(x) + 1


def integration(x):
    return sp.trapz(x)


x = np.arange(-3, 3, 0.01)
y = f(x)
#Y = integration(y)
plt.plot(x, y)
#plt.plot(x, Y)
plt.show()
