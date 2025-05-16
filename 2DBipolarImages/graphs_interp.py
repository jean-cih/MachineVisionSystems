import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import RegularGridInterpolator


def intensity_plot(y_positions: np.ndarray, x: list, intensities: np.ndarray):

    f = RegularGridInterpolator((y_positions, x), intensities)

    x_new = np.linspace(min(x), max(x), 100)
    y_new = np.linspace(0, 4, 100)
    x_grid, y_grid = np.meshgrid(x_new, y_new)

    points = np.stack((y_grid, x_grid), axis=-1)
    interpolated_image = f(points)

    plt.imshow(interpolated_image, extent=[min(x_new), max(x_new), 0, 4], origin='lower', aspect='auto', cmap='viridis')
    plt.colorbar(label="Интенсивность")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Интерполированное поле интенсивности")
    plt.show()


if __name__ == '__main__':

    x = list(range(-4, 5))
    y_data = [
        [0, 1, 1, -2, 2, 0, -1, -1, 0],
        [0, 0, -2, 2, 4, 0, 0, -4, 0],
        [0, -1, 0, 0, 0, -2, 2, 1, 0],
        [0, 0, -2, 2, 0, 2, -2, 0, 0],
        [0, -1, 0, 1, 0, 1, 0, -1, 0]
    ]

    y_positions = np.linspace(0, 4, 5)

    intensities = np.array(y_data)

    intensity_plot(y_positions, x, intensities)


