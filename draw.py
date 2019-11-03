import numpy as np
import sys, pygame
from random import shuffle, random
from matplotlib.colors import hsv_to_rgb
from mover import Person
from math_fns import *

pygame.init()

size = width, height = 512, 512
speed = 2
black = 0, 0, 0

screen = pygame.display.set_mode(size)

path_s = pygame.Surface(size)
surface = pygame.Surface(size)

time = 0
people_count = 12
dist_from_center = 128

rand_order = list(range(people_count))
shuffle(rand_order)

people = [Person(dist_from_center*ang_to_vec(360*i/people_count),
                 dist_from_center*ang_to_vec(360*rand_order[i]/people_count),
                 color=255*hsv_to_rgb(np.array([i/people_count,random()/2+0.5,random()/2+0.5])))
          for i in range(people_count)]

main_surface = True

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                path_s.fill((0,0,0))
                shuffle(rand_order)
                for i, person in enumerate(people):
                    person.end = dist_from_center*ang_to_vec(360*rand_order[i]/people_count)
            elif event.key == pygame.K_w:
                main_surface ^= True

    time += 1

    surface.fill((0,0,0))
    for person in people:
        person.calculate(people)

    for person in people:
        person.step()
        person.draw()

    screen.fill(black)
    screen.blit(surface if main_surface else path_s, pygame.Rect((0,0), size))
    pygame.display.flip()
