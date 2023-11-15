from svg.path import parse_path
from xml.dom.minidom import parse
import numpy as np
from matplotlib import pyplot as plt

def read_svg_file(file_path):
    """
    Function to read an SVG file and extract the path data.

    Parameters:
    file_path (str): The path to the SVG file.

    Returns:
    list: A list of points (x, y) along the SVG path.
    """
    # Parse the SVG file
    doc = parse(file_path)

    # Find the first <path> element and get its 'd' attribute
    path_strings = doc.getElementsByTagName('path')
    d_string = path_strings[0].getAttribute('d')

    # Parse the path data into a list of path objects
    path_data = parse_path(d_string)

    # Initialize an empty list to hold the points
    points = []

    # Number of points to interpolate per segment
    num_points = 10

    # Iterate over the path objects
    for path in path_data:
        # If the path object is a Line or a CubicBezier, we can interpolate points along the path
        if hasattr(path, 'start') and hasattr(path, 'end'):
            for t in np.linspace(0, 1, num_points):
                point = path.point(t)
                points.append((point.real, point.imag))
        # If the path object is an Arc, we need to approximate it with a series of points
        elif hasattr(path, 'center'):
            theta1 = np.angle(path.start - path.center)
            theta2 = np.angle(path.end - path.center)
            thetas = np.linspace(theta1, theta2, num_points)
            for theta in thetas:
                point = path.center + path.radius * np.exp(1j * theta)
                points.append((point.real, point.imag))

    # Plot the points
    plt.figure(figsize=(8, 8))
    plt.scatter(*zip(*points), s=1)
    plt.title('Points extracted from SVG path')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

    return points