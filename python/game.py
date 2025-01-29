import pygame
from OpenGL.GL import *
# from OpenGL.GLUT import *
# from OpenGL.GLU import *
# import numpy as np

# Initialize pygame
pygame.init()

# Set the window size
width, height = 800, 800

# Create the Pygame window
screen = pygame.display.set_mode((width, height), pygame.DOUBLEBUF | pygame.OPENGL)

# Set up the OpenGL perspective
# gluOrtho2D(0, width, 0, height)
