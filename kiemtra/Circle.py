import math
from Shape import Shape


class Circle(Shape):
    def __init__(self,x,y,banKinh): 
        super().__init__(x,y)
        self.banKinh = banKinh

    def chuVi(self):
        chuVi = 2 * math.pi * self.banKinh
        return chuVi
    
    def dienTich(self):
        dienTich = self.banKinh * self.banKinh * math.pi
        return dienTich