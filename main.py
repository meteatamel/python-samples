from shapes.square import Square
from shapes.shape_factory import ShapeFactory

if __name__ == "__main__":

    obj = Square(2)
    print(obj)

    obj = ShapeFactory.create_shape("circle")
    print(obj)
