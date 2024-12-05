print("Sinh vien:Van Tuan DAt")
print("MSSV: 235752021610083")
###################

# Hàm kiểm tra nếu số nhị phân chia hết cho 5
def is_divisible_by_5(binary_str):
    decimal = int(binary_str, 2)
    return decimal % 5 == 0

# Nhập chuỗi nhị phân
binary_input = input("Nhập chuỗi nhị phân 4 chữ số, phân tách bằng dấu phẩy: ")
binary_list = binary_input.split(',')

# Kiểm tra và in các số chia hết cho 5
result = [binary for binary in binary_list if is_divisible_by_5(binary)]
print(','.join(result))

