from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_circumference(self):
        pass

    @abstractmethod
    def __str__(self):
        pass
