import numpy as np
import matplotlib.pyplot as plt
from Code.Approximation_Ableitung.Derivative import Derivative


def f(x):
    return np.power(x, 4)


def df(x):
    return 4*np.power(x, 3)


def ddf(x):
    return 12*np.power(x, 2)


h1 = 0.001
h2 = 0.002
h3 = 0.003
x = np.linspace(0, 2, 100)

y_point_1 = Derivative.of_order_1(f, 1, h1)
y_point_2 = Derivative.of_order_1(f, 0.75, h1)
y_real_1 = df(1)
y_real_2 = df(0.75)

y_min = 0
y_max = 13

fig1, (ax1, ax2) = plt.subplots(1, 2)
fig1.suptitle('Analytische und numerische erste Ableitung im Punkt', fontweight='bold')

ax1.plot(x, df(x), label=r'$f´(x) = 4x^3$', color='orange')
ax1.plot(1, y_real_1, 'go')
ax1.plot(0.75, y_real_2, 'go')

ax1.set_ylim([y_min, y_max])
ax1.grid()
ax1.legend()

ax2.plot(x, df(x), label=r'$f´(x) = 4x^3$', color='orange')
ax2.plot(1, y_point_1, 'ro')
ax2.plot(0.75, y_point_2, 'ro')

ax2.set_ylim([y_min, y_max])
ax2.grid()
ax2.legend()

#plt.show()

y_point_1 = Derivative.of_order_2(f, 1, h1)
y_point_2 = Derivative.of_order_2(f, 0.75, h1)
y_real_1 = ddf(1)
y_real_2 = ddf(0.75)

fig2, (ax1, ax2) = plt.subplots(1, 2)
fig2.suptitle('Analytische und numerische zweite Ableitung im Punkt', fontweight='bold')

ax1.plot(x, ddf(x), label=r'$f´´(x) = 12x^2$', color='orange')
ax1.plot(1, y_real_1, 'go')
ax1.plot(0.75, y_real_2, 'go')

ax1.set_ylim([y_min, y_max])
ax1.grid()
ax1.legend()

ax2.plot(x, ddf(x), label=r'$f´´(x) = 12x^2$', color='orange')
ax2.plot(1, y_point_1, 'ro')
ax2.plot(0.75, y_point_2, 'ro')

ax2.set_ylim([y_min, y_max])
ax2.grid()
ax2.legend()

#plt.show()

y_point_1 = Derivative.of_order_2(f, 0.75, h1)
y_point_2 = Derivative.of_order_2(f, 0.75, h2)
y_point_3 = Derivative.of_order_2(f, 0.75, h3)
y_real = ddf(0.75)

x = np.linspace(0.5, 1, 100)
y_min = 6.75 - 1/np.power(10, 4.7)
y_max = 6.75 + 1/np.power(10, 4.7)

plt.figure()
plt.title('Fehler der Approximation infinitesimal nah an 6.75', fontweight='bold')

plt.plot(x, ddf(x), label=r'$f´´(x) = 12x^2$', color='orange')
plt.plot(0.75, y_real, 'go', label=f'Analytisch')
plt.plot(0.75, y_point_1, 'yo', label=f'h = 0.001')
plt.plot(0.75, y_point_2, 'ro', label=f'h = 0.002')
plt.plot(0.75, y_point_3, 'bo', label=f'h = 0.003')

plt.ylim([y_min, y_max])
plt.grid()
plt.legend()

plt.show()
