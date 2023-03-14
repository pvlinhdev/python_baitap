import math
from Shape import Shape

class Triangle(Shape):
    def __init__(self ,x,y,a,b,c): 
        super().__init__(x,y)
        self.a = a
        self.b = b
        self.c = c

    def chuVi(self):
        chuVi = self.a + self.b + self.c
        return chuVi
        
    def dienTich(self):
        p = self.a + self.b + self.c / 2
        dienTich = math.sqrt(p* (p-self.a) * (p-self.b) * (p-self.c))
        return dienTich