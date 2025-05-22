from shapes.shape import Shape
import math

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def get_area(self):
        return math.pi * (self.radius ** 2)

    def get_circumference(self):
        return 2 * math.pi * self.radius

    def __str__(self):
        return f"Circle: radius={self.radius}, color={self.color}"
