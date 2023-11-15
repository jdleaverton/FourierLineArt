
from setuptools import setup, find_packages

setup(
    name='FourierLineArt',
    version='1.0',
    description='A Python program that takes an SVG file, extracts points from its outline, fits a Fourier series to these points, and then animates the drawing of the series.',
    author='JD Leaverton',
    author_email='jdleaverton@gmail.com',
    url='http://github.com/yourusername/FourierLineArt',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'matplotlib',
        'scipy',
        'svg.path',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3.6',
)

