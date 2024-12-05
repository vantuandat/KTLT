print("Sinh vien:Van Tuan Dat")
print("MSSV:235752021610083")
##################


import math

class Circle:
    def __init__(self, radius):
        self.radius = radius  # Khởi tạo bán kính
    
    def area(self):
        # Tính diện tích hình tròn
        return math.pi * (self.radius ** 2)
    
    def circumference(self):
        # Tính chu vi hình tròn
        return 2 * math.pi * self.radius

# Tạo đối tượng Circle với bán kính là 7
circle = Circle(7)

# In diện tích và chu vi của hình tròn
print(f"Diện tích của hình tròn là: {circle.area():.2f}")
print(f"Chu vi của hình tròn là: {circle.circumference():.2f}")
