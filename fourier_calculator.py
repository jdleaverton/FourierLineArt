
import numpy as np

def calculate_fourier_coefficients(complex_points, num_coefficients):
    """
    Function to calculate the Fourier coefficients of a list of complex numbers.

    Parameters:
    complex_points (list): A list of complex numbers representing the points.
    num_coefficients (int): The number of Fourier coefficients to calculate.

    Returns:
    list: A list of complex Fourier coefficients.
    """
    # Convert the complex points to a numpy array for easier manipulation
    complex_points = np.array(complex_points)

    # Determine the total number of points
    T = len(complex_points)

    # Initialize an array to store the Fourier coefficients
    coefficients = np.zeros(num_coefficients, dtype=complex)

    # Calculate the Fourier coefficients
    for n in range(num_coefficients):
        for t in range(T):
            coefficients[n] += complex_points[t] * np.exp(-1j * 2 * np.pi * n * t / T)
        coefficients[n] /= T

    return coefficients.tolist()

