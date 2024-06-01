import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import LightSource
from Code.Approximation_Ableitung.Derivative import Derivative


def l1(x: np.ndarray) -> np.ndarray:
    """
    Linear function for the first segment.
    :param x: x value
    :return: output of the linear function
    """
    return 2.5 * x + 3.75


def l2(x: np.ndarray) -> np.ndarray:
    """
    Linear function for the second segment.
    :param x: x value
    :return: output of the linear function
    """
    return -2.5 * x + 3.75


def deformation_function(x: np.ndarray) -> np.ndarray:
    """
    Deformation function that models the shape of the deformed metal sheet.
    :param x: x value
    :return: output array of z values representing the deformation
    """
    z = np.zeros_like(x)
    mask1 = (-1.5 < x) & (x < -1.3)
    mask2 = (-1.3 <= x) & (x <= 1.3)
    mask3 = (1.3 < x) & (x < 1.5)

    z[mask1] = l1(x[mask1])
    z[mask2] = 0.5
    z[mask3] = l2(x[mask3])

    return z


def temperature_function(x: np.ndarray, z: np.ndarray) -> np.ndarray:
    """
    Function to calculate the temperature distribution based on deformation.
    :param x: x value
    :param z: z value
    :return: output array of temperature values
    """
    h = 0.01
    gradient = np.abs(Derivative.of_order_1(deformation_function, x, h)) / 2.5
    temperature = gradient - z
    temperature[(-1.3 <= x) & (x <= 1.3)] = 0.4
    temperature = 1000 * temperature + 20
    return temperature


# Anwendungsbeispiel: Simulation der Blechverformung
def plot_simulation_metal_deformation():
    """
    Plot the simulation of the temperature distribution on a deformed metal sheet.

    This function creates a 3D surface plot of the deformation and overlays a color map
    representing the temperature distribution.
    """
    x = np.linspace(-5, 5, 500)
    y = np.linspace(-5, 5, 100)
    x, y = np.meshgrid(x, y)

    z = deformation_function(x)

    temperature = temperature_function(x, z)

    ls = LightSource(azdeg=315, altdeg=45)
    rgb = ls.shade(z, cmap=cm.jet, vert_exag=1, blend_mode='overlay')

    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111, projection='3d')

    surf = ax.plot_surface(
        x,
        y,
        z,
        rstride=1,
        cstride=1,
        facecolors=plt.cm.jet(temperature / 1000),
        linewidth=0,
        antialiased=True,
        shade=False
    )

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    ax.set_zlim(0, 2)

    ax.set_title('Simulation der Temperaturverteilung an einem verformten Stück Blech.')

    plt.subplots_adjust(right=0.8)

    cbar_ax = fig.add_axes([0.85, 0.15, 0.03, 0.7])
    m = plt.cm.ScalarMappable(cmap=plt.cm.jet)
    m.set_array(temperature)
    fig.colorbar(m, cax=cbar_ax)

    ax.view_init(elev=30, azim=135)

    plt.show()


plot_simulation_metal_deformation()
