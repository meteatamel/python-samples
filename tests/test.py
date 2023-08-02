import sys

sys.path.append("../")
from shapes.square import Square
from shapes.shape_factory import ShapeFactory

def test_basic():
    obj = Square(2)
    print(obj)

    obj = ShapeFactory.create_shape("circle")
    print(obj)