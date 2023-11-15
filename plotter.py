from matplotlib import pyplot as plt
import numpy as np
from matplotlib import animation

def animate_fourier_series(fourier_coefficients, reconstructed_path):
    """
    Function to animate the drawing of the Fourier series.

    Parameters:
    fourier_coefficients (list): A list of complex Fourier coefficients.
    reconstructed_path (list): A list of points representing the reconstructed path.

    Returns:
    None
    """
    # Convert the Fourier coefficients and reconstructed path to numpy arrays for easier manipulation
    fourier_coefficients = np.array(fourier_coefficients)
    reconstructed_path = np.array(reconstructed_path)

    # Create a figure and axis for the animation
    fig, ax = plt.subplots()

    # Initialize a line for the reconstructed path and a collection of lines for the rotating vectors
    path_line, = ax.plot([], [], 'r-')
    vector_lines = [ax.plot([], [], 'g-')[0] for _ in range(len(fourier_coefficients))]

    # Calculate the range of the data
    x_range = reconstructed_path.real.max() - reconstructed_path.real.min()
    y_range = reconstructed_path.imag.max() - reconstructed_path.imag.min()

    # Calculate the center of the data
    x_center = (reconstructed_path.real.max() + reconstructed_path.real.min()) / 2
    y_center = (reconstructed_path.imag.max() + reconstructed_path.imag.min()) / 2

    # Calculate the maximum range and the margin
    max_range = max(x_range, y_range)
    margin = max_range * 0.2  # 20% margin

    # Set the axis limits
    ax.set_xlim(x_center - max_range / 2 - margin, x_center + max_range / 2 + margin)
    ax.set_ylim(y_center - max_range / 2 - margin, y_center + max_range / 2 + margin)

    # Ensure the aspect ratio is equal
    ax.set_aspect('equal', adjustable='datalim')

    # Function to initialize the animation
    def init():
        path_line.set_data([], [])
        for line in vector_lines:
            line.set_data([], [])
        return [path_line] + vector_lines

    # Function to update the animation for each frame
    def update(frame):
        # Update the path line
        path_line.set_data(reconstructed_path.real[:frame], reconstructed_path.imag[:frame])

        # Calculate the positions of the rotating vectors
        vectors = np.zeros_like(fourier_coefficients, dtype=complex)
        for n in range(len(fourier_coefficients)):
            vectors[n] = fourier_coefficients[n] * np.exp(1j * 2 * np.pi * n * frame / len(reconstructed_path))

        # Calculate the cumulative sum of the vectors
        cumulative_vectors = np.cumsum(vectors)

        # Update the vector lines
        for n, line in enumerate(vector_lines):
            if n == 0:
                line.set_data([0, vectors[n].real], [0, vectors[n].imag])
            else:
                line.set_data([cumulative_vectors[n-1].real, cumulative_vectors[n].real], [cumulative_vectors[n-1].imag, cumulative_vectors[n].imag])

        return [path_line] + vector_lines

    # Create the animation
    ani = animation.FuncAnimation(fig, update, frames=len(reconstructed_path), init_func=init, blit=True, interval=50)
    # Save the animation as a GIF
    ani.save('animation.gif', writer='pillow')
    
    # Show the animation
    plt.show()