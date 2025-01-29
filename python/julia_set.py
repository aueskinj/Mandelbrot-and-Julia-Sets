"""
julia_set.py

This module generates and visualizes Julia sets using PyOpenGL for rendering with Pygame.

Functions:
-----------
julia(c, width, height, max_iter, escape_radius):
    Generates the Julia set for a given complex constant c.

render_julia_set():
    Renders the Julia set using PyOpenGL and Pygame.

Constants:
-----------
DEFAULT_WIDTH (int): Default width of the Julia set window.
DEFAULT_HEIGHT (int): Default height of the Julia set window.
"""

import numpy as np
import pygame
from pygame.locals import *
from OpenGL.GL import *

# Constants for the Julia set rendering
DEFAULT_WIDTH = 800
DEFAULT_HEIGHT = 600

def julia(c, width=DEFAULT_WIDTH, height=DEFAULT_HEIGHT, max_iter=300, escape_radius=2.0):
    """
    Generates a Julia set for a given complex constant c.

    Parameters:
        c (complex): The constant for the Julia set equation f(z) = z^2 + c.
        width (int): The width of the rendered image.
        height (int): The height of the rendered image.
        max_iter (int): Maximum number of iterations for each point.
        escape_radius (float): The radius beyond which a point escapes.

    Returns:
        np.ndarray: A 2D array representing iteration counts for each point.
    """
    x_range = np.linspace(-2, 2, width)
    y_range = np.linspace(-2, 2, height)
    julia_data = np.zeros((height, width), dtype=np.int32)

    for i, y in enumerate(y_range):
        for j, x in enumerate(x_range):
            z = complex(x, y)
            iter_count = 0
            while abs(z) <= escape_radius and iter_count < max_iter:
                z = z**2 + c
                iter_count += 1
            julia_data[i, j] = iter_count

    return julia_data

def render_julia_set():
    """
    Renders the Julia set using PyOpenGL and Pygame.
    """
    pygame.init()
    screen = pygame.display.set_mode((DEFAULT_WIDTH, DEFAULT_HEIGHT), DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Julia Set")

    glClearColor(0, 0, 0, 1)
    glOrtho(-1, 1, -1, 1, -1, 1)

    # Generate Julia set data
    c = complex(-0.7, 0.27015)  # Example constant for the Julia set
    julia_data = julia(c, DEFAULT_WIDTH, DEFAULT_HEIGHT)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        # Clear the screen
        glClear(GL_COLOR_BUFFER_BIT)
        glBegin(GL_POINTS)

        for i in range(DEFAULT_HEIGHT):
            for j in range(DEFAULT_WIDTH):
                iter_count = julia_data[i, j]
                color_intensity = iter_count / np.max(julia_data)
                glColor3f(color_intensity, color_intensity * 0.5, 1.0 - color_intensity)
                glVertex2f(j / DEFAULT_WIDTH * 2 - 1, i / DEFAULT_HEIGHT * 2 - 1)

        glEnd()
        pygame.display.flip()

    pygame.quit()
