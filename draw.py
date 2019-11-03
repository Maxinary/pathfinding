import sys, pygame
from mover import Person
from math_fns import *

# define constants
black = (0, 0, 0)

pygame.init()

size = width, height = 512, 512

# Set up surface
screen = pygame.display.set_mode(size)
surface = pygame.Surface(size)

time = 0

while 1:
    time += 1
    # parse key presses
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    # calculate movement
    for person in people:
        person.calculate(people)

    # move and draw
    surface.fill((0,0,0))
    for person in people:
        person.step()
        person.draw(surface)

    screen.blit(surface if main_surface else path_s, pygame.Rect((0,0), size))
    pygame.display.flip()
