print("Sinh vien:Van Tuan DAt")
print("MSSV: 235752021610083")
###################


# Nhập một chuỗi các phần tử từ bàn phím và chuyển nó thành list
input_list = input("Nhập các phần tử, cách nhau bởi dấu cách: ").split()

# Cắt list: lấy list nhưng bỏ phần tử đầu và cuối
if len(input_list) > 2:  # Đảm bảo có ít nhất 3 phần tử để cắt
    cut_list = input_list[1:-1]
    print("List sau khi cắt phần tử đầu và cuối:", cut_list)
else:
    print("List không đủ phần tử để cắt (phải có ít nhất 3 phần tử).")

