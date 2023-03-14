import random

def random_input_file(fileName, num_shapes):
    shapes = ["#Rect", "#Circle", "#Triangle"]
    with open(fileName, "w") as file:
        for i in range(num_shapes):
            shape = random.choice(shapes)
            file.write(shape + "\n")
            if shape == "#Rect":
                rong = random.randint(1, 10)
                dai = random.randint(1, 10)
                x = random.randint(-20, 20)
                y = random.randint(-20, 20)
                file.write(str(rong) + " " + str(dai) + "\n")
                file.write(str(x) + " " + str(y) + "\n")
            elif shape == "#Circle":
                banKinh = random.randint(1, 10)
                x = random.randint(-20, 20)
                y = random.randint(-20, 20)
                file.write(str(banKinh) + "\n")
                file.write(str(x) + " " + str(y) + "\n")
            elif shape == "#Triangle":
                a, b, c = 0, 0, 0
                while (a + b <= c) or (a + c <= b) or (b + c <= a):
                    a = random.randint(1, 10)
                    b = random.randint(1, 10)
                    c = random.randint(1, 10)
                x = random.randint(-20, 20)
                y = random.randint(-20, 20)
                file.write(str(a) + " " + str(b) + " " + str(c) + "\n")
                file.write(str(x) + " " + str(y) + "\n")

random_input_file("kiemtra/input.txt",20)

