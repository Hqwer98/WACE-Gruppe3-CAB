from typing import Callable

import numpy as np
import matplotlib.pyplot as plt
from Code.Approximation_Integral.Newton_Cotes.SimpsonRule import SimpsonRule

l = 10  #Meter
q_0 = 2  #Newton/Meter
simpson = SimpsonRule(node_count=100)


def q(x: float) -> float:
    return (q_0 * (l - x)) / l


def Q(x: float) -> float:
    return -1 * simpson.calculate_integral_composite(q, x, l)


def M(x: float) -> float:
    return simpson.calculate_integral_simple(Q, x, l)


def plot_internal_forces():
    x = np.linspace(0, l, 100)

    q_values = np.array([q(i) for i in x])
    Q_values = np.array([Q(i) for i in x])
    M_values = np.array([M(i) for i in x])

    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 6))

    ax1.plot(x, q_values, label=r'Streckenlast $q(x)$', color='r')
    ax1.set_ylabel(r'$q (N/M)$')
    ax1.fill_between(x, q_values, color='red', alpha=0.2, label=r'$\int q(x) dx$')
    ax1.legend()
    ax1.grid()

    ax2.plot(x, Q_values, label=r'Querkraftverlauf $Q(x)$', color='r')
    ax2.set_ylabel(r'$Q (N)$')
    ax2.fill_between(x, Q_values, color='red', alpha=0.2, label=r'$\int Q(x) dx$')
    ax2.legend()
    ax2.grid()

    ax3.plot(x, M_values, label=r'Momentverlauf $M(x)$', color='r')
    ax3.set_xlabel(r'$x (m)$')
    ax3.set_ylabel(r'$M (Nm)$')
    ax3.fill_between(x, M_values, color='red', alpha=0.2, label=r'$\int M(x) dx$')
    ax3.legend()
    ax3.grid()

    plt.tight_layout()
    plt.show()


plot_internal_forces()
