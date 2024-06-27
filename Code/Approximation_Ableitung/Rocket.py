import numpy as np
import matplotlib.pyplot as plt
from Code.Approximation_Ableitung.Derivative import Derivative

rt = np.array([0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240])
rh = np.array([0, 0.8, 3.5, 8.4, 15.5, 25.1, 36.8, 50.2, 64.0, 77.2, 90.7, 104, 118]) * 1000
rv = np.array([0, 321, 674, 1147, 1795, 2695, 3832, 5164, 6219, 7790, 9769, 12235, 14356]) / 3.6


def f(x):
    return np.interp(x, rt, rv)


h = 1
ra = Derivative.of_order_1(f, rt, h)

rocket_plotting_time = []
rocket_plotting_height = []
rocket_plotting_velocity = []
rocket_plotting_acceleration = []

for i in range(len(rt)):
    if rt[i] <= 200:
        rocket_plotting_time.append(rt[i])
        rocket_plotting_height.append(rh[i])
        rocket_plotting_velocity.append(rv[i])
        rocket_plotting_acceleration.append(ra[i])

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 8))

ax1.plot(rocket_plotting_time, rocket_plotting_height, 'o', label='Raketen Höhe')
ax1.plot(rocket_plotting_time, rocket_plotting_height)
ax1.legend(loc='best')
ax1.grid()
ax1.set_ylabel(r"Höhe in $m$")

ax2.plot(rocket_plotting_time, rocket_plotting_velocity, 'o', label='Raketen Geschwindigkeit')
ax2.plot(rocket_plotting_time, rocket_plotting_velocity)
ax2.legend(loc='best')
ax2.grid()
ax2.set_ylabel(r"Geschwindigkeit in $m/s$")

ax3.plot(rocket_plotting_time, rocket_plotting_acceleration, 'o', label='Raketen Beschleunigung')
ax3.plot(rocket_plotting_time, rocket_plotting_acceleration)
ax3.legend(loc='best')
ax3.grid()
ax3.set_ylabel(r"Beschleunigung in $m/s^2$")
ax3.set_xlabel(r"Zeit in $s$")

plt.show()
