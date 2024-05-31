import numpy as np
import matplotlib.pyplot as plt
from Code.Approximation_Ableitung.Derivative import Derivative
from typing import Callable


def l1(x):
    return 2.5 * x + 3.75


def l2(x):
    return -2.5 * x + 3.75


#Anwendungsbeispiel: Simulation der Blechverformung
def plot_simulation_metal_deformation():
    # Create a grid of x and y values
    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    x, y = np.meshgrid(x, y)

    # Define a function that simulates the metal deformation
    def deformation_function(x, y):
        z = np.zeros_like(x)
        mask1 = (-1.5 < x) & (x < -1.3)
        mask2 = (-1.3 <= x) & (x <= 1.3)
        mask3 = (1.3 < x) & (x < 1.5)

        z[mask1] = l1(x[mask1])
        z[mask2] = 0.5
        z[mask3] = l2(x[mask3])

        return z

    # Define a function that simulates the temperature distribution
    def temperature_function(x, y, z):
        return np.sin(x) * np.cos(y)

    # Calculate z values based on the deformation function
    z = deformation_function(x, y)

    # Calculate temperature values
    temperature = temperature_function(x, y, z)

    # Plot the deformation using a 3D surface plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Plot the surface with temperature-based color mapping
    surf = ax.plot_surface(x, y, z, facecolors=plt.cm.jet(
        (temperature - temperature.min()) / (temperature.max() - temperature.min())), edgecolor='none')

    # Add a color bar to indicate the temperature scale
    mappable = plt.cm.ScalarMappable(cmap='jet')
    mappable.set_array(temperature)
    fig.colorbar(mappable, ax=ax, shrink=0.5, aspect=5)

    # Set labels for the axes
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    ax.set_zlim(0, 2)

    # Set the title of the plot
    ax.set_title('Simulation of Metal Sheet Deformation with Non-Isothermal Temperature Distribution')

    # Show the plot
    plt.show()


plot_simulation_metal_deformation()
