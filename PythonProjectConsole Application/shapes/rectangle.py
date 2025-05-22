from shapes.shape import Shape

class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_circumference(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return f"Rectangle: width={self.width}, height={self.height}, color={self.color}"
