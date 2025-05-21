class Student:
    def __init__(self, ten, diem_toan, diem_van, diem_anh):
        self.ten = ten
        self.diem_toan = diem_toan
        self.diem_van = diem_van
        self.diem_anh = diem_anh

    def tinh_diem_trung_binh(self):
        return (self.diem_toan + self.diem_van + self.diem_anh) / 3

    def hien_thi_thong_tin(self):
        print("Tên:", self.ten)
        print("Điểm Toán:", self.diem_toan)
        print("Điểm Văn:", self.diem_van)
        print("Điểm Anh:", self.diem_anh)
        print("Điểm trung bình:", self.tinh_diem_trung_binh())

ten = input("Nhập tên học sinh: ")
diem_toan = float(input("Nhập điểm Toán: "))
diem_van = float(input("Nhập điểm Văn: "))
diem_anh = float(input("Nhập điểm Anh: "))

hoc_sinh = Student(ten, diem_toan, diem_van, diem_anh)

hoc_sinh.hien_thi_thong_tin()