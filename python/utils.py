"""
utils.py

This module provides utility functions for managing the OpenGL rendering window,
handling user inputs, and other shared tasks for the Julia and Mandelbrot sets.

Functions:
-----------
initialize_window(width, height, title):
    Creates and initializes an OpenGL rendering window using Pygame.

handle_key_input(event):
    Processes key inputs for controlling the rendering or interacting with the visualization.

check_for_errors():
    Checks for OpenGL errors and logs them.
"""

import pygame
import logging
import sys
from OpenGL.GL import *

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

def initialize_window(width, height, title):
    """
    Creates and initializes an OpenGL rendering window using Pygame.

    Parameters:
        width (int): The width of the window in pixels.
        height (int): The height of the window in pixels.
        title (str): The title of the window.

    Returns:
        pygame.Surface: The created Pygame window surface.
    """
    pygame.init()
    pygame.display.set_mode((width, height), pygame.OPENGL | pygame.DOUBLEBUF)
    pygame.display.set_caption(title)

    # Configure OpenGL viewport
    glViewport(0, 0, width, height)
    glEnable(GL_DEPTH_TEST)

    logging.info(f"OpenGL window '{title}' initialized ({width}x{height})")
    return pygame.display.get_surface()

def handle_key_input(event):
    """
    Processes key inputs for controlling the rendering or interacting with the visualization.

    Parameters:
        event (pygame.event.Event): The event object from Pygame.
    
    Behavior:
        - Pressing 'ESCAPE' key closes the application.
    """
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            logging.info("Escape key pressed. Exiting...")
            pygame.quit()
            sys.exit()

def check_for_errors():
    """
    Checks for OpenGL errors and logs them.

    Raises:
        RuntimeError: If an OpenGL error is detected.
    """
    error = glGetError()
    if error != GL_NO_ERROR:
        logging.error(f"OpenGL error detected: {error}")
        raise RuntimeError(f"OpenGL error detected: {error}")
