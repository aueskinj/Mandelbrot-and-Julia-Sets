import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((800, 600), DOUBLEBUF | OPENGL)
clock = pygame.time.Clock()

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()

    # Draw your OpenGL scene here

    pygame.display.flip()
    clock.tick(60)
