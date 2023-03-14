from abc import ABC,abstractclassmethod

class Shape(ABC):

    def __init__(self, x , y):
        self.x = x
        self.y = y

    @abstractclassmethod
    def chuVi():
        pass
    @abstractclassmethod
    def dienTich():
        pass