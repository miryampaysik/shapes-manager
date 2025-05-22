from shapes.square import Square
from shapes.rectangle import Rectangle
from shapes.circle import Circle
from shapes.triangle import RightTriangle


class ShapeManager:
    def __init__(self):
        self.shapes = []

    def add_shape(self):
        print("\nSelect shape to add:")
        print("1. Square")
        print("2. Rectangle")
        print("3. Circle")
        print("4. Right Triangle")
        choice = input("Enter choice (1-4): ")

        color = input("Enter color: ")

        if choice == "1":
            width = float(input("Enter width: "))
            shape = Square(color, width)
        elif choice == "2":
            width = float(input("Enter width: "))
            height = float(input("Enter height: "))
            shape = Rectangle(color, width, height)
        elif choice == "3":
            radius = float(input("Enter radius: "))
            shape = Circle(color, radius)
        elif choice == "4":
            width = float(input("Enter width: "))
            height = float(input("Enter height: "))
            shape = RightTriangle(color, width, height)
        else:
            print("Invalid choice!")
            return

        self.shapes.append(shape)
        print(f"Added {shape}")

    def list_all_shapes(self):
        if not self.shapes:
            print("No shapes to list.")
        else:
            for shape in self.shapes:
                print(shape)

    def sum_all_circumferences(self):
        total = sum(shape.get_circumference() for shape in self.shapes)
        print(f"Total circumference of all shapes: {total}")

    def sum_all_areas(self):
        total = sum(shape.get_area() for shape in self.shapes)
        print(f"Total area of all shapes: {total}")

    def find_biggest_circumference(self):
        if not self.shapes:
            print("No shapes to compare.")
            return
        biggest = max(self.shapes, key=lambda shape: shape.get_circumference())
        print(f"Largest circumference: {biggest.get_circumference()}")
        print(f"Shape: {biggest}")

    def find_biggest_area(self):
        if not self.shapes:
            print("No shapes to compare.")
            return
        biggest = max(self.shapes, key=lambda shape: shape.get_area())
        print(f"Largest area: {biggest.get_area()}")
        print(f"Shape: {biggest}")
