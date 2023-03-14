from models.person import Person

class Student(Person):
    def __init__(self, id, code, firstName, lastName, birthOfDate, Toan, Ly, Hoa):
        super().__init__(id, code, firstName, lastName, birthOfDate)
        self.Toan = Toan
        self.Ly = Ly
        self.Hoa = Hoa
        