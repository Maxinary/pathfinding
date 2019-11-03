import sys, pygame
import numpy as np
from random import shuffle, random
from matplotlib.colors import hsv_to_rgb

pygame.init()

size = width, height = 512, 512
speed = 2
black = 0, 0, 0

screen = pygame.display.set_mode(size)

path_s = pygame.Surface(size)
surface = pygame.Surface(size)

def rotate(points, angle):
    theta = np.radians(angle)
    c, s = np.cos(theta), np.sin(theta)
    R = np.array(((c,-s), (s, c)))
    return np.array([R @ p for p in points])

def translate(points, x_translation, y_translation):
    return np.array([(x+x_translation, y+y_translation) for (x, y) in points])

def scale(points, x_scale, y_scale):
    R = np.array(((x_scale,0), (0, y_scale)))
    return np.array([R @ p for p in points])

def ang_to_vec(angle):
    theta = np.radians(angle)

    return np.array([np.cos(theta), np.sin(theta)])

def sign(x):
    return 1 if x > 0 else -1

time = 0

class Person:
    def __init__(self, start, end, color=[None]):
        if None in color:
            color = [random()*255, random()*255, random()*255]
        self.pos = np.array(start, dtype=np.float64)
        self.end = np.array(end)
        self.velocity = np.zeros(2)

        self.max_speed = 2*(1.75+random()*0.5)
        self.mass = 0.2*(0.9+random()*0.2)

        self.color = pygame.Color(int(color[0]),
                                  int(color[1]),
                                  int(color[2]))

    def draw(self):
        pts = [[-1, 0],[-0.5, 0.866],[ 0.5, 0.866],
               [ 1, 0],[ 0.5,-0.866],[-0.5,-0.866]]
        pygame.draw.polygon(surface,
                            pygame.Color(255,0,0),
                            translate(
                                translate(
                                    scale(
                                        pts,
                                        8, 8),
                                    self.pos[0], self.pos[1]),
                                width/2, height/2
                                ))
    def step(self):
        start = self.pos.copy()
        speed = np.linalg.norm(self.velocity)
        if speed > self.max_speed:
            self.velocity *= self.max_speed/speed
        self.pos += self.velocity

        pygame.draw.line(path_s, self.color,
                         translate([start], width/2, height/2)[0],
                         translate([self.pos], width/2, height/2)[0])

    def apply(self, force):
        self.velocity += force / self.mass

    def calculate(self, people):
        d_from_goal = np.linalg.norm(self.end - self.pos)
        self.velocity *= 1-1/(1+d_from_goal/4)
        if d_from_goal > 4:
            forces = np.zeros(2)
            forces += (self.end - self.pos)/d_from_goal

            speed = np.linalg.norm(self.velocity)

            for person in people:
                if person != self:
                    difference = person.pos-self.pos
                    distance = np.linalg.norm(difference)
                    forces -= difference/(distance/7)**3

                    combined_speed = self.velocity @ person.velocity.T

                    forces -= 3*difference/(distance**2)

            self.apply(forces)

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
