from pygame import draw
from math_fns import translate, scale

class Shape:
    def __init__(self, species = None):
        self.species = species

    def draw(self, surface):
        raise Exception("No drawing function implemented")

class Circle(Shape):
    def __init__(self, center, radius):
        super().__init__(self, "Circle")
        self.pos = np.array(center, dtype = np.float64)
        self.radius = radius

    def draw(self, surface):
        draw.circle(surface, self.color, self.pos, self.radius)

class Rectangle(Shape):
    def __init__(self, c1, c2):
        super().__init__(self, "Rectangle")
        self.pos = np.array([(c1[0]+c2[0])/2,(c1[1]+c2[1])/2], dtype = np.float64)
        self.width = abs(c1[0]-c2[0])
        self.height = abs(c1[1]-c2[1])

    def draw(self, surface):
        corners = [c1, [c1[0], c2[1]], c2, [c1[1], c2[0]]]
        draw.polygon(surface, self.color, corners)
