print("Sinh vien:Van Tuan DAt")
print("MSSV: 235752021610083")
###################

import find_max  # Nhập module find_max

def main():
    # Nhập số lượng phần tử của danh sách
    n = int(input("Nhập số lượng phần tử của danh sách: "))
    
    # Nhập các phần tử của danh sách
    lst = []
    for i in range(n):
        value = int(input(f"Nhập phần tử thứ {i + 1}: "))
        lst.append(value)
    
    # Tìm phần tử lớn nhất và nhỏ nhất
    max_value = find_max.find_max(lst)
    min_value = min(lst)  # Dùng hàm min để tìm phần tử nhỏ nhất

    # Tìm vị trí của phần tử lớn nhất và nhỏ nhất
    max_index = lst.index(max_value)  # Vị trí của phần tử lớn nhất
    min_index = lst.index(min_value)  # Vị trí của phần tử nhỏ nhất

    # In kết quả
    print(f"Phần tử lớn nhất trong danh sách là: {max_value}, vị trí: {max_index + 1}")
    print(f"Phần tử nhỏ nhất trong danh sách là: {min_value}, vị trí: {min_index + 1}")

if __name__ == "__main__":
    main()

