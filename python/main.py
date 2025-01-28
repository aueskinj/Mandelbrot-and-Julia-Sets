# main.py

"""
main.py

This is the entry point for the Fractal Viewer application. It uses PyOpenGL and Pygame to render
interactive visualizations of Julia and Mandelbrot sets. Users can switch between the two fractals
and explore their fascinating patterns.

Functions:
-----------
main():
    Initializes the Pygame display and OpenGL settings, handles user inputs, and renders the
    chosen fractal (Mandelbrot or Julia set).

Key Features:
-------------
- Press '1': Render the Mandelbrot set.
- Press '2': Render the Julia set.
- Press 'ESC': Exit the application.

Requirements:
-------------
- pygame
- PyOpenGL
- numpy
- Other dependencies specified in requirements.txt

Usage:
------
Run the script directly using Python:
    python main.py
"""

import sys
import glfw
from OpenGL.GL import *
from julia_set import render_julia_set
from mandelbrot_set import render_mandelbrot_set

def main():
    # Initialize GLFW
    if not glfw.init():
        print("Failed to initialize GLFW")
        sys.exit(1)

    # Create a windowed mode window and its OpenGL context
    window = glfw.create_window(800, 600, "Julia and Mandelbrot Sets", None, None)
    if not window:
        print("Failed to create GLFW window")
        glfw.terminate()
        sys.exit(1)

    # Make the window's context current
    glfw.make_context_current(window)

    # Set the clear color
    glClearColor(0.0, 0.0, 0.0, 1.0)

    # Select which set to render
    print("Select the fractal to render:")
    print("1. Julia Set")
    print("2. Mandelbrot Set")
    choice = input("Enter your choice (1 or 2): ").strip()

    if choice == "1":
        render_function = render_julia_set
    elif choice == "2":
        render_function = render_mandelbrot_set
    else:
        print("Invalid choice. Exiting.")
        glfw.terminate()
        sys.exit(1)

    # Main loop
    while not glfw.window_should_close(window):
        # Clear the screen
        glClear(GL_COLOR_BUFFER_BIT)

        # Render the selected fractal
        render_function()

        # Swap front and back buffers
        glfw.swap_buffers(window)

        # Poll for and process events
        glfw.poll_events()

    # Terminate GLFW
    glfw.terminate()

if __name__ == "__main__":
    main()
