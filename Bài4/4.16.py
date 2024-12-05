print("Sinh vien:Van Tuan DAt")
print("MSSV: 235752021610083")
###################


# Nhập chuỗi các số nhị phân từ người dùng
input_string = input("Nhập chuỗi các số nhị phân, cách nhau bởi dấu phẩy: ")

# Tách chuỗi thành danh sách các số nhị phân
binary_numbers = input_string.split(',')

# In ra các số nhị phân đã tách
print("Các số nhị phân đã nhập:")
for binary in binary_numbers:
    print(binary)
