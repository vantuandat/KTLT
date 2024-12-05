print("Sinh vien:Van Tuan Dat")
print("MSSV: 235752021610083")
###################


# Nhập một chuỗi các phần tử từ bàn phím và chuyển nó thành list
input_list = input("Nhập các phần tử, cách nhau bởi dấu cách: ").split()

# Nhập phần tử muốn thêm vào list
new_element = input("Nhập phần tử muốn thêm vào list: ")

# Thêm phần tử vào cuối list
input_list.append(new_element)

# In list sau khi thêm phần tử
print("List sau khi thêm phần tử:", input_list)
