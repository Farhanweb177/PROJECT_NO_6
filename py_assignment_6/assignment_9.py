from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def Area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def Area(self):
        return self.width + self.height
    
result = Rectangle(50, 82)
print("Result: ", result.Area())