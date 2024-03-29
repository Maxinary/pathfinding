import numpy
from pygame import draw
from random import random
from math_fns import translate, scale

class Shape:
    def __init__(self, species = None, color = [None]):
        self.species = species
        if None in color:
            color = [random()*255, random()*255, random()*255]

    def draw(self, surface):
        raise Exception("No drawing function implemented")

class Circle(Shape):
    def __init__(self, center, radius, color = [None]):
        super().__init__(self, "Circle", color)
        self.pos = np.array(center, dtype = np.float64)
        self.radius = radius

    def draw(self, surface):
        draw.circle(surface, self.color, self.pos, self.radius)

class Rectangle(Shape):
    def __init__(self, c1, c2, color = [None]):
        super().__init__(self, "Rectangle", color)
        self.pos = np.array([(c1[0]+c2[0])/2,(c1[1]+c2[1])/2], dtype = np.float64)
        self.width = abs(c1[0]-c2[0])
        self.height = abs(c1[1]-c2[1])
        self.left = min(c1[0], c2[0])
        self.right = max(c1[0], c2[0])
        self.top = min(c1[1], c2[1])
        self.bottom = max(c1[1], c2[1])

def collide(shapeA, shapeB):
    if shapeA.species == None or shapeB.species == None:
        raise "Cannot collide NoneType shapes"
    else if shapeA.species == "Circle" and shapeB.species == "Circle":
        return circle_collide(shapeA, shapeB)
    else if shapeA.species == "Rectangle" and shapeB.species == "Rectangle":
        return rectangle_collide(shapeA, shapeB)
    else if shapeA.species == "Circle":
        return circle_rectangle_collide(shapeA, shapeB)
    else:
        return circle_rectangle_collide(shapeB, shapeA)

def circle_collide(a, b):
    dist = Math.sqrt(np.sum((a.pos - b.pos)**2))
    return dist <= a.radius + b.radius

def rectangle_collide(a, b):

    def draw(self, surface):
        corners = [c1, [c1[0], c2[1]], c2, [c1[1], c2[0]]]
        draw.polygon(surface, self.color, corners)
