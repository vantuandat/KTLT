print("Sinh vien:Van Tuan DAt")
print("MSSV: 235752021610083")
###################

# Hàm cộng hai số
def add(x, y):
    return x + y

# Hàm trừ hai số
def subtract(x, y):
    return x - y

# Hàm nhân hai số
def multiply(x, y):
    return x * y

# Hàm chia hai số
def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Không thể chia cho 0"

# Menu cho người dùng chọn phép toán
print("Chọn phép toán:")
print("1. Cộng")
print("2. Trừ")
print("3. Nhân")
print("4. Chia")

# Nhập lựa chọn của người dùng
choice = input("Nhập lựa chọn (1/2/3/4): ")

# Nhập các số cần tính toán
num1 = float(input("Nhập số thứ nhất: "))
num2 = float(input("Nhập số thứ hai: "))

# Tính toán và hiển thị kết quả dựa trên lựa chọn
if choice == '1':
    print(f"Kết quả: {add(num1, num2)}")
elif choice == '2':
    print(f"Kết quả: {subtract(num1, num2)}")
elif choice == '3':
    print(f"Kết quả: {multiply(num1, num2)}")
elif choice == '4':
    print(f"Kết quả: {divide(num1, num2)}")
else:
    print("Lựa chọn không hợp lệ")
