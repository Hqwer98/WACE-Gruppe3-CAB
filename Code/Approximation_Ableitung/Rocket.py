import numpy as np
import matplotlib.pyplot as plt
from Code.Approximation_Ableitung.Derivative import Derivative

rt = np.array([0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60])
rh = np.array([0, 0, 0.1, 0.4, 0.8, 1.3, 1.9, 2.6, 3.5, 4.5, 5.6, 6.9, 8.4]) * 1000
rv = np.array([0, 32, 145, 250, 321, 396, 480, 570, 674, 786, 906, 1041, 1147]) / 3.6


def f(x):
    return 0.04 * np.power(x, 3)


ra = Derivative.of_order_2(f, rt, 0.01)

t = np.linspace(0, 60, 50)

h = f(t)

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 8))

ax1.plot(t, h, label=r"$f(t)$")
ax1.plot(rt, rh, 'o', label='Raketen Höhe')

ax1.legend(loc='best')
ax1.grid()

ax1.set_ylabel(r"Höhe in $m$")

dh = Derivative.of_order_1(f, t, 0.01)

ax2.plot(t, dh, label=r"$f'(t)$")
ax2.plot(rt, rv, 'o', label='Raketen Geschwindigkeit')

ax2.legend(loc='best')
ax2.grid()

ax2.set_ylabel(r"Geschwindigkeit in $m/s$")

ddh = Derivative.of_order_2(f, t, 0.01)

ax3.plot(t, ddh, label=r"$f''(t)$")
ax3.plot(rt, ra, 'o', label='Raketen Beschleunigung')

ax3.legend(loc='best')
ax3.grid()

ax3.set_ylabel(r"Beschleunigung in $m/s^2$")
ax3.set_xlabel(r"Zeit in $s$")

plt.show()
