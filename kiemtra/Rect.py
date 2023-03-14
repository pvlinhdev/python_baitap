from Shape import Shape

class Rect(Shape):
    def __init__(self ,x,y,dai,rong): 
        super().__init__(x,y)
        self.dai = dai
        self.rong = rong
    
    def chuVi(self):
        chuVi = (self.dai + self.rong) * 2
        return chuVi
    
    def dienTich(self):
        dienTich = self.dai * self.rong
        return dienTich