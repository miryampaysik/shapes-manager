from shapes.shape import Shape

class Square(Shape):
    def __init__(self, color, width):
        super().__init__(color)
        self.width = width

    def get_area(self):
        return self.width ** 2

    def get_circumference(self):
        return self.width * 4

    def __str__(self):
        return f"Square: width={self.width}, color={self.color}"
