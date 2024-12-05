print("Sinh vien:Van Tuan Dat")
print("MSSV: 235752021610083")
###################



# Nhập một chuỗi các phần tử từ bàn phím và chuyển nó thành list
input_list = input("Nhập các phần tử, cách nhau bởi dấu cách: ").split()

# Nhập phần tử muốn xóa khỏi list
remove_element = input("Nhập phần tử muốn xóa khỏi list: ")

# Kiểm tra và xóa phần tử khỏi list
if remove_element in input_list:
    input_list.remove(remove_element)
    print("List sau khi xóa phần tử:", input_list)
else:
    print(f"Phần tử '{remove_element}' không có trong list.")

