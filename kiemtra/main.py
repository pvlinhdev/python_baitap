from Circle import Circle
from Rect import Rect
from Triangle import Triangle
shapes = []
def docfile(file):
    
    with open(file, 'r') as f:
        while True:
            line = f.readline().strip()
            if not line:
                break
            
            if line == '#Circle':
                banKinh = float(f.readline().strip())
                x, y = map(float, f.readline().strip().split())
                shapes.append(Circle( x, y,banKinh))
            
            elif line == '#Rect':
                rong, dai = map(float, f.readline().strip().split())
                x, y = map(float, f.readline().strip().split())
                shapes.append(Rect( x, y,rong, dai))
            
            elif line == '#Triangle':
                a, b, c = map(float, f.readline().strip().split())
                x, y = map(float, f.readline().strip().split())
                shapes.append(Triangle( x, y,a, b, c))
    return shapes


data = docfile("kiemtra/input.txt")
print(data)
print("--------------")
def lietke():
    # Liệt kê hình có chu vi lớn nhất và diện tích lớn nhất
    max_chu_vi = max(shapes, key=lambda x: x.chuVi()).chuVi()
    max_dien_tich = max(shapes, key=lambda x: x.dienTich()).dienTich()
    print(f"Hình có chu vi lớn nhất: {max_chu_vi}")
    print(f"Hình có diện tích lớn nhất: {max_dien_tich}")


# Kiểm tra số lượng hình nằm chồng lên nhau nhiều 
def kiemTra():
    max_overlap_count = 0
    for i in range(len(shapes)):
        overlap_count = 0
        for j in range(i + 1, len(shapes)):
            if shapes[i].overlap(shapes[j]):
                overlap_count += 1
        max_overlap_count = max(max_overlap_count, overlap_count)
    print(f"Số lượng hình nằm chồng lên nhau nhiều nhất: {max_overlap_count}")

lietke()

print("--------------")

kiemTra()


