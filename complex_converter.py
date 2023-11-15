
import numpy as np

def convert_to_complex(points):
    """
    Function to convert a list of points (x, y) to a list of complex numbers.

    Parameters:
    points (list): A list of points (x, y).

    Returns:
    list: A list of complex numbers representing the points.
    """
    # Convert the points to a numpy array for easier manipulation
    points = np.array(points)

    # Convert each point (x, y) to a complex number (x + iy)
    complex_points = points[:, 0] + 1j * points[:, 1]

    return complex_points.tolist()

