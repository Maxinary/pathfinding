

class Shape:
    def __init__(self, species = None):
        self.species = species

class Circle(Shape):
    def __init__(self, center, radius):
        super().__init__(self, "Circle")
        self.pos = np.array(center, dtype = np.float64)
        self.radius = radius

class Rectangle(Shape):
    def __init__(self, c1, c2):
        super().__init__(self, "Rectangle")
        self.pos = np.array([(c1[0]+c2[0])/2,(c1[1]+c2[1])/2], dtype = np.float64)
        self.width = abs(c1[0]-c2[0])
        self.height = abs(c1[1]-c2[1])
