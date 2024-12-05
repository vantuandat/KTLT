print("Sinh vien:Van Tuan Dat")
print("MSSV: 235752021610083")
###################


# Nhập một chuỗi các phần tử từ bàn phím và chuyển nó thành list
input_list = input("Nhập các phần tử, cách nhau bởi dấu cách: ").split()

# Nhập phần tử muốn tìm kiếm
search_element = input("Nhập phần tử muốn tìm: ")

# Tìm vị trí của phần tử trong list
try:
    index_position = input_list.index(search_element)
    print(f"Phần tử '{search_element}' có trong list tại vị trí {index_position}.")
except ValueError:
    print(f"Phần tử '{search_element}' không có trong list.")

