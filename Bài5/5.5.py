print("Sinh vien:Van Tuan DAt")
print("MSSV: 235752021610083")
###################

# main.py

# Nhập module mymodule
import mymodule

# Bước 1: Nhập số lượng phần tử và giá trị của danh sách
n = int(input("Nhập số lượng phần tử trong danh sách: "))
lst = []

# Nhập các phần tử vào danh sách
for i in range(n):
    value = int(input(f"Nhập phần tử thứ {i+1}: "))
    lst.append(value)

# Bước 2: Sử dụng các hàm trong module mymodule để tìm max, min và sắp xếp danh sách
max_value = mymodule.find_max(lst)
min_value = mymodule.find_min(lst)
sorted_lst = mymodule.sort_list(lst)

# Bước 3: In kết quả
print(f"Phần tử lớn nhất trong danh sách: {max_value}")
print(f"Phần tử nhỏ nhất trong danh sách: {min_value}")
print(f"Danh sách sau khi sắp xếp: {sorted_lst}")
