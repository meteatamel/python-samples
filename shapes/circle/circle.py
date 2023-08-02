import sys
import math

sys.path.append("../../") # Needed for main method to work in this class
from shapes.shape import Shape

class Circle(Shape):

    def __init__(self, radius):
        if radius < 1:
            raise Exception("Radius less than 1")
        self.radius = radius

    def __str__(self):
        return f"circle with area: {self.get_area()}"

    def get_area(self) -> float:
        return math.pi * self.radius * self.radius

if __name__ == "__main__":
    obj = Circle(2)
    print(obj)
