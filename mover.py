import numpy as np
from random import shuffle, random
from pygame import Color, draw

class Body:
    def __init__(self, start_position, color=[None], shape):
        self.pos = np.array(start_position, dtype = np.float64)
        self.color = color

    def draw(surface):
        raise "Unimplemented draw method call"

    
class KinematicBody(Body):

class Mover(KinematicBody):
    def __init__(self, start_position, color=[None]):
        self.pos = np.array(start_position, dtype = np.float64)
        self.color = color
        self.velocity = np.zeros(2)
        

    def draw(surface):
        raise "Unimplemented draw method call"

class Person(Mover):
    def __init__(self, start, end, color=[None]):
        if None in color:
            color = [random()*255, random()*255, random()*255]
        self.pos = np.array(start, dtype=np.float64)
        self.end = np.array(end)
        self.velocity = np.zeros(2)

        self.max_speed = 2*(1.75+random()*0.5)
        self.mass = 0.2*(0.9+random()*0.2)

        self.color = Color(int(color[0]),
                                  int(color[1]),
                                  int(color[2]))

    #probably needs to be decomposed better
    def draw(self):
        pass

    def step(self):
        start = self.pos.copy()
        speed = np.linalg.norm(self.velocity)
        if speed > self.max_speed:
            self.velocity *= self.max_speed/speed
        self.pos += self.velocity

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
