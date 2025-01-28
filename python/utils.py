# utils.py
"""
utils.py

This module provides utility functions for managing the OpenGL rendering window,
handling user inputs, and other shared tasks for the Julia and Mandelbrot sets.

Functions:
    initialize_window(width, height, title):
        Creates and initializes an OpenGL rendering window using GLFW.

    handle_key_input(window, key, scancode, action, mods):
        Processes key inputs for controlling the rendering or interacting with the visualization.

    check_for_errors():
        Checks for OpenGL errors and logs them.
"""

import glfw
from OpenGL.GL import *
import sys

def initialize_window(width, height, title):
    """
    Creates and initializes an OpenGL rendering window using GLFW.

    Parameters:
        width (int): The width of the window in pixels.
        height (int): The height of the window in pixels.
        title (str): The title of the window.

    Returns:
        GLFWwindow: The created GLFW window object.

    Raises:
        RuntimeError: If the window cannot be created.
    """
    if not glfw.init():
        raise RuntimeError("Failed to initialize GLFW.")

    # Set GLFW window hints
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    # Create the window
    window = glfw.create_window(width, height, title, None, None)
    if not window:
        glfw.terminate()
        raise RuntimeError("Failed to create GLFW window.")

    # Make the OpenGL context current
    glfw.make_context_current(window)

    # Enable V-Sync
    glfw.swap_interval(1)

    # Configure viewport
    glViewport(0, 0, width, height)

    return window

def handle_key_input(window, key, scancode, action, mods):
    """
    Processes key inputs for controlling the rendering or interacting with the visualization.

    Parameters:
        window (GLFWwindow): The GLFW window object.
        key (int): The key being pressed or released.
        scancode (int): The platform-specific scan code of the key.
        action (int): The action (press, release, or repeat).
        mods (int): Bitfield describing which modifier keys are held down.

    Behavior:
        - Pressing the 'ESCAPE' key closes the window.
    """
    if key == glfw.KEY_ESCAPE and action == glfw.PRESS:
        glfw.set_window_should_close(window, True)

def check_for_errors():
    """
    Checks for OpenGL errors and logs them.

    Raises:
        RuntimeError: If an OpenGL error is detected.
    """
    error = glGetError()
    if error != GL_NO_ERROR:
        raise RuntimeError(f"OpenGL error detected: {error}")
