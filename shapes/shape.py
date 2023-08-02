from abc import ABC, abstractmethod

class Shape(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def get_area(self):
        pass

if __name__ == "__main__":
    obj = Shape()
    print(obj)
