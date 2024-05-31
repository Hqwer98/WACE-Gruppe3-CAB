import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import LightSource
from Code.Approximation_Ableitung.Derivative import Derivative
from typing import Callable


def l1(x):
    return 2.5 * x + 3.75


def l2(x):
    return -2.5 * x + 3.75


def deformation_function(x):
    z = np.zeros_like(x)
    mask1 = (-1.5 < x) & (x < -1.3)
    mask2 = (-1.3 <= x) & (x <= 1.3)
    mask3 = (1.3 < x) & (x < 1.5)

    z[mask1] = l1(x[mask1])
    z[mask2] = 0.5
    z[mask3] = l2(x[mask3])

    return z


def temperature_function(x, z) -> np.ndarray:
    h = 0.01
    gradient = np.abs(Derivative.of_order_1(deformation_function, x, h)) / 2.5
    temperature = gradient - z
    temperature[(-1.3 <= x) & (x <= 1.3)] = 0.4

    # Normalize temperature to a realistic range (e.g., 0 to 1000°C)
    temperature = 1000 * temperature
    return temperature


# Anwendungsbeispiel: Simulation der Blechverformung
def plot_simulation_metal_deformation():
    # Create a grid of x and y values
    x = np.linspace(-5, 5, 500)
    y = np.linspace(-5, 5, 100)
    x, y = np.meshgrid(x, y)

    # Calculate z values based on the deformation function
    z = deformation_function(x)

    # Calculate temperature values
    temperature = temperature_function(x, z)

    # Create a light source for shading
    ls = LightSource(azdeg=315, altdeg=45)
    rgb = ls.shade(z, cmap=cm.jet, vert_exag=1, blend_mode='overlay')

    # Plot the deformation using a 3D surface plot
    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111, projection='3d')

    # Plot the surface with the temperature as the colormap
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

    # Set labels for the axes
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    ax.set_zlim(0, 2)

    # Set the title of the plot
    ax.set_title('Simulation der Temperaturverteilung an einem verformten Stück Blech.')

    # Add a color bar which maps values to colors
    m = plt.cm.ScalarMappable(cmap=plt.cm.jet)
    m.set_array(temperature)
    fig.colorbar(m, ax=ax, shrink=0.5, aspect=5)

    # Adjust the view angle for better visualization
    ax.view_init(elev=30, azim=135)

    # Show the plot
    plt.show()


plot_simulation_metal_deformation()
