
import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

def resample_points(points, num_points):
    """
    Function to resample the points along the SVG path.

    Parameters:
    points (list): A list of points (x, y) along the SVG path.
    num_points (int): The number of points to be used in the Fourier series.

    Returns:
    list: A resampled list of points.
    """
    # Convert the points to a numpy array for easier manipulation
    points = np.array(points)

    # Compute the cumulative distance along the path
    distance = np.cumsum(np.sqrt(np.sum(np.diff(points, axis=0)**2, axis=1)))
    distance = np.insert(distance, 0, 0)/distance[-1]

    # Interpolate the x and y coordinates separately
    fx, fy = interp1d(distance, points[:, 0]), interp1d(distance, points[:, 1])

    # Create an array of evenly spaced points along the path
    alpha = np.linspace(0, 1, num_points)

    # Resample the points
    resampled_points = np.column_stack([fx(alpha), fy(alpha)])

    # Calculate the centroid of the resampled points
    centroid = np.mean(resampled_points, axis=0)

    # Subtract the centroid from each point to ensure the centroid is at the origin
    resampled_points -= centroid

    return resampled_points.tolist()