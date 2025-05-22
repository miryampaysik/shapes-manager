from shapes.shape import Shape
import math

class RightTriangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height

    def get_area(self):
        return 0.5 * self.width * self.height

    def get_circumference(self):
        hypotenuse = math.sqrt(self.width ** 2 + self.height ** 2)
        return self.width + self.height + hypotenuse

    def __str__(self):
        return f"Right Triangle: width={self.width}, height={self.height}, color={self.color}"
