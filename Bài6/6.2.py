print("Sinh vien:Van Tuan Dat")
print("MSSV:235752021610083")
##################



class Hinhchunhat(object):
    def __init__(self, dai, rong):
        # Khởi tạo đối tượng với chiều dài và chiều rộng
        self.dai = dai
        self.rong = rong
    
    def area(self):
        # Phương thức tính diện tích
        return self.dai * self.rong  # Công thức diện tích A = dài * rộng

# Tạo một đối tượng Hinhchunhat với chiều dài 5 và chiều rộng 3
hinh = Hinhchunhat(5, 3)

# In diện tích của hình chữ nhật
print(hinh.area())
