import sys

sys.path.append("../") # Needed for main method to work in this class
from shapes.square import Square
from shapes.circle.circle import Circle

class ShapeFactory():

    @staticmethod
    def create_shape(type):
        if type == "square":
            return Square(2)
        if type == "circle":
            return Circle(2)
        raise Exception(f"Unknown type: {type}")

if __name__ == "__main__":
    obj = ShapeFactory.create_shape("square")
    print(obj)

    obj = ShapeFactory.create_shape("circle")
    print(obj)
