from manim.manim import *
import numpy as np

class FourierSeries(Scene):
    def __init__(self, fourier_coefficients, reconstructed_path, renderer):
        super().__init__(renderer)
        self.fourier_coefficients = fourier_coefficients
        self.reconstructed_path = reconstructed_path
        # Convert complex Fourier coefficients to real numbers

    def construct(self):
        # Sort the Fourier coefficients by frequency
        sorted_coefficients = sorted(enumerate(self.real_fourier_coefficients), key=lambda x: abs(x[1]))

        # Create a group to hold the circles and lines
        group = VGroup()

        # Create the circles and lines
        for n, coeff in sorted_coefficients:
            circle = Circle(radius=abs(coeff)).shift(RIGHT * abs(coeff))
            line = Line(circle.get_center(), circle.get_center() + circle.radius * RIGHT, color=YELLOW)
            rotating_line = Line(circle.get_center(), circle.get_center() + circle.radius * RIGHT, color=RED)
            rotating_line.add_updater(lambda m, dt: m.rotate(coeff * dt, about_point=circle.get_center()))
            group.add(circle, line, rotating_line)

        # Create a path to trace the end of the last line
        path = VMobject()
        path.set_points_as_corners([group[-1].get_end()])

        # Add everything to the scene
        self.add(group, path)

        # Function to update the circles and lines for each frame
        def update_group(group, dt):
            for i in range(2, len(group), 3):
                group[i-2].next_to(group[i-1], RIGHT, buff=0)
                group[i].next_to(group[i-2], RIGHT, buff=0)
            path.add_smooth_curve_to(group[-1].get_end())

        # Animate the group
        group.add_updater(update_group)
        self.wait(len(self.real_reconstructed_path))

        # Remove the updater
        group.clear_updaters()

    