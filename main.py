
import argparse
import logging
from svg_reader import read_svg_file
from resampler import resample_points
from complex_converter import convert_to_complex
from fourier_calculator import calculate_fourier_coefficients
from path_reconstructor import reconstruct_path
from plotter import animate_fourier_series

def main():
    logging.basicConfig(level=logging.INFO)
    parser = argparse.ArgumentParser(description='A Python program that takes an SVG file, extracts points from its outline, fits a Fourier series to these points, and then animates the drawing of the series.')
    parser.add_argument('file_path', type=str, help='The path to the SVG file.')
    parser.add_argument('--num_points', type=int, default=1000, help='The number of points to be used in the Fourier series.')
    parser.add_argument('--num_coefficients', type=int, default=100, help='The number of Fourier coefficients to compute.')
    args = parser.parse_args()

    logging.info('Reading SVG file and extracting path data...')
    points = read_svg_file(args.file_path)

    logging.info('Resampling points along the SVG path...')
    points = resample_points(points, args.num_points)

    logging.info('Converting points to complex numbers...')
    complex_points = convert_to_complex(points)

    logging.info('Computing Fourier coefficients...')
    coefficients = calculate_fourier_coefficients(complex_points, args.num_coefficients)
    logging.info('Fourier coefficients: {}'.format([str(coefficient) for coefficient in coefficients]))
    
    logging.info('Reconstructing the path using the Fourier series...')
    reconstructed_path = reconstruct_path(coefficients, args.num_points)

    logging.info('Plotting the drawing of the Fourier series...')
    animate_fourier_series(coefficients, reconstructed_path)

    '''
    from manim import config
    from manim.renderer.cairo_renderer import CairoRenderer
    from manim import FourierSeries

    logging.info('Plotting and animating the drawing of the Fourier series...')
    # Set the output file
    config.output_file = "output"

    # Set the renderer to 'cairo'
    config.renderer = "cairo"

    # Create a renderer
    renderer = CairoRenderer()

    # Create an instance of your scene with your arguments
    scene = FourierSeries(coefficients, reconstructed_path, renderer)

    # Render the scene
    scene.render()
    '''

if __name__ == "__main__":
    main()

