print("Sinh vien:Van Tuan Dat")
print("MSSV:235752021610083")
##################

class Circle(object):
    def __init__(self, r):
        # Khởi tạo đối tượng với bán kính r
        self.radius = r
    
    def area(self):
        # Phương thức tính diện tích
        return self.radius**2 * 3.14  # Công thức diện tích A = π * r^2

# Tạo một đối tượng Circle với bán kính 2
aCircle = Circle(2)

# In diện tích của hình tròn
print(aCircle.area())
