import numpy as np
import matplotlib.pyplot as plt
from Code.Approximation_Ableitung.Derivative import Derivative


def f(x):
    return np.square(x)


def df(x):
    return 2 * x


def ddf(x):
    return np.full_like(x, 2)


h = 0.0001
x = np.linspace(0, 4, 100)

y_real_1 = df(x)
y_real_2 = ddf(x)

y_approximated_1 = Derivative.of_order_1(f, x, h)
y_approximated_2 = Derivative.of_order_2(f, x, h)

y_min = 0
y_max = 8

fig1, (ax1, ax2) = plt.subplots(1, 2)
fig1.suptitle('Analytische und numerische erste Ableitung', fontweight='bold')

ax1.plot(x, y_real_1, 'b', label=r'$f´(x) = 2x$')

ax1.set_ylim([y_min, y_max])
ax1.grid()
ax1.legend()

ax2.plot(x, y_approximated_1, 'r', label=r'$f´(x) \approx 2x$')

ax2.set_ylim([y_min, y_max])
ax2.grid()
ax2.legend()

plt.show()

fig2, (ax1, ax2) = plt.subplots(1, 2)
fig2.suptitle('Analytische und numerische zweite Ableitung', fontweight='bold')

ax1.plot(x, y_real_2, 'b', label=r'$f´´(x) = 2$')

ax1.set_ylim([y_min, y_max])
ax1.grid()
ax1.legend()

ax2.plot(x, y_approximated_2, 'r', label=r'$f´´(x) \approx 2$')

ax2.set_ylim([y_min, y_max])
ax2.grid()
ax2.legend()

plt.show()

y_min = 2 - 1/np.power(10, 6)
y_max = 2 + 1/np.power(10, 6)

fig2, (ax1, ax2) = plt.subplots(1, 2)
fig2.suptitle('Fehler der Approximation infinitesimal nah an 2', fontweight='bold')

ax1.plot(x, y_real_2, 'b', label=r'$f´´(x) = 2$')

ax1.set_ylim([y_min, y_max])
ax1.grid()
ax1.legend()

ax2.plot(x, y_approximated_2, 'r', label=r'$f´´(x) \approx 2$')

ax2.set_ylim([y_min, y_max])
ax2.grid()
ax2.legend()

plt.show()
