# mandelbrot_set.py
"""
mandelbrot_set.py

This module generates and visualizes Mandelbrot sets using PyOpenGL for rendering.

Functions:
    mandelbrot(width, height, max_iter, escape_radius):
        Generates the Mandelbrot set for a given window in the complex plane.

    render_mandelbrot(mandelbrot_data, width, height):
        Renders the Mandelbrot set data using PyOpenGL.

Constants:
    DEFAULT_WIDTH (int): Default width of the Mandelbrot set window.
    DEFAULT_HEIGHT (int): Default height of the Mandelbrot set window.
"""

import numpy as np
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Constants for the Mandelbrot set rendering
DEFAULT_WIDTH = 800
DEFAULT_HEIGHT = 600

def mandelbrot(width=DEFAULT_WIDTH, height=DEFAULT_HEIGHT, max_iter=300, escape_radius=2.0):
    """
    Generates the Mandelbrot set for a given window in the complex plane.

    Parameters:
        width (int): The width of the rendered image.
        height (int): The height of the rendered image.
        max_iter (int): Maximum number of iterations for each point.
        escape_radius (float): The radius beyond which a point escapes.

    Returns:
        np.ndarray: A 2D array representing iteration counts for each point.
    """
    x_range = np.linspace(-2.5, 1.5, width)
    y_range = np.linspace(-2, 2, height)
    mandelbrot_data = np.zeros((height, width), dtype=np.int32)

    for i, y in enumerate(y_range):
        for j, x in enumerate(x_range):
            c = complex(x, y)
            z = 0
            iter_count = 0
            while abs(z) <= escape_radius and iter_count < max_iter:
                z = z**2 + c
                iter_count += 1
            mandelbrot_data[i, j] = iter_count

    return mandelbrot_data

def render_mandelbrot(mandelbrot_data, width=DEFAULT_WIDTH, height=DEFAULT_HEIGHT):
    """
    Renders the Mandelbrot set data using PyOpenGL.

    Parameters:
        mandelbrot_data (np.ndarray): The 2D array of iteration counts.
        width (int): Width of the rendered image.
        height (int): Height of the rendered image.
    """
    def display():
        glClear(GL_COLOR_BUFFER_BIT)
        glBegin(GL_POINTS)

        for i in range(height):
            for j in range(width):
                iter_count = mandelbrot_data[i, j]
                color_intensity = iter_count / np.max(mandelbrot_data)
                glColor3f(color_intensity * 0.7, color_intensity * 0.4, 1.0 - color_intensity)
                glVertex2f(j / width * 2 - 1, i / height * 2 - 1)

        glEnd()
        glFlush()

    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(width, height)
    glutCreateWindow("Mandelbrot Set")
    glClearColor(0, 0, 0, 1)
    glOrtho(-1, 1, -1, 1, -1, 1)
    glutDisplayFunc(display)
    glutMainLoop()
