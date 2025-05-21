class CayCanh:
    def __init__(self, ten, tinh_trang, gia):
        self.ten = ten
        self.tinh_trang = tinh_trang 
        self.gia = gias

    def mo_ta(self):
        return f"Tên: {self.ten}, Tình trạng: {self.tinh_trang}, Giá: {self.gia} đồng"

class QuanLyVuon:
    def __init__(self):
        self.danh_sach_cay = []

    def them_cay(self, cay):
        if cay.gia >= 0:
            self.danh_sach_cay.append(cay)
            print(f"Đã thêm cây '{cay.ten}' vào vườn.")
        else:
            print("Giá cây không hợp lệ.")

    def xem_danh_sach_cay(self):
        if not self.danh_sach_cay:
            print("Vườn chưa có cây nào.")
            return
        print("\n--- Danh sách cây trong vườn ---")
        for i, cay in enumerate(self.danh_sach_cay):
            print(f"{i+1}. {cay.mo_ta()}")
        print("-----------------------------\n")

    def cham_soc_cay(self, ten_cay, tinh_trang_moi):
        for cay in self.danh_sach_cay:
            if cay.ten.lower() == ten_cay.lower():
                cay.tinh_trang = tinh_trang_moi
                print(f"Đã cập nhật tình trạng của cây '{cay.ten}' thành '{tinh_trang_moi}'.")
                return
        print(f"Không tìm thấy cây '{ten_cay}' trong vườn.")

quan_ly = QuanLyVuon()

while True:
    print("\n--- CHƯƠNG TRÌNH QUẢN LÝ VƯỜN CÂY ---")
    print("1. Thêm cây mới")
    print("2. Xem danh sách cây")
    print("3. Chăm sóc cây (cập nhật tình trạng)")
    print("4. Thoát")

    lua_chon = input("Nhập lựa chọn của bạn: ")

    if lua_chon == '1':
        ten = input("Nhập tên cây: ")
        tinh_trang = input("Nhập tình trạng cây (sống, chết, hạt mầm, đã bán): ")
        while True:
            try:
                gia = int(input("Nhập giá cây (phải từ 200 đồng trở lên): "))
                if gia >= 200:
                    break
                else:
                    print("Giá cây phải từ 200 đồng trở lên.")
            except ValueError:
                print("Vui lòng nhập một số nguyên cho giá.")
        cay_moi = CayCanh(ten, tinh_trang, gia)
        quan_ly.them_cay(cay_moi)

    elif lua_chon == '2':
        quan_ly.xem_danh_sach_cay()

    elif lua_chon == '3':
        ten_cay_cham_soc = input("Nhập tên cây cần chăm sóc: ")
        tinh_trang_moi = input("Nhập tình trạng mới của cây: ")
        quan_ly.cham_soc_cay(ten_cay_cham_soc, tinh_trang_moi)

    elif lua_chon == '4':
        print("Cảm ơn bạn đã sử dụng chương trình!")
        break

    else:
        print("Lựa chọn không hợp lệ. Vui lòng thử lại.")