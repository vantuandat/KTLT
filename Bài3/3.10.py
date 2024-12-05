print("Sinh vien:Van Tuan DAt")
print("MSSV: 235752021610083")
###################





import math

def Tinh(R):
    # Kiểm tra bán kính hợp lệ (bán kính phải là số dương)
    if R <= 0:
        print("Bán kính phải là số dương lớn hơn 0.")
        return
    
    # Tính chu vi và diện tích hình tròn
    chu_vi = 2 * math.pi * R
    dien_tich = math.pi * R * R
    
    # In kết quả
    print(f"Chu vi hình tròn là: {chu_vi:.2f}")
    print(f"Diện tích hình tròn là: {dien_tich:.2f}")

# Nhập bán kính từ người dùng
R = float(input("Nhập bán kính hình tròn: "))
Tinh(R)
