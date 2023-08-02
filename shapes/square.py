import sys

sys.path.append("../") # Needed for main method to work in this class
from shapes.shape import Shape

class Square(Shape):

    def __init__(self, side):
        self.side = side

    def __str__(self):
        return f"square with area: {self.get_area()}"

    def get_area(self) -> float:
        return self.side * self.side

if __name__ == "__main__":
    obj = Square(2)
    print(obj)
