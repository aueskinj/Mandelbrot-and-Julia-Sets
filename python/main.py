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
import pygame
from pygame.locals import *
from OpenGL.GL import *
from julia_set import render_julia_set
from mandelbrot_set import render_mandelbrot_set

def main():
    # Initialize Pygame
    pygame.init()

    # Set up the display with OpenGL
    screen = pygame.display.set_mode((800, 600), DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Julia and Mandelbrot Sets")

    # Set the clear color (black background)
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
        pygame.quit()
        sys.exit(1)

    # Main loop
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

        # Render the selected fractal
        render_function()

        # Swap buffers (update display)
        pygame.display.flip()

    # Quit Pygame
    pygame.quit()
    sys.exit(0)

if __name__ == "__main__":
    main()
