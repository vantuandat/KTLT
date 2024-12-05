print("Sinh vien:Van Tuan Dat")
print("MSSV:235752021610083")
##################




# main.py
import binary_search  # Nhập module binary_search

def main():
    # Nhập số lượng phần tử của danh sách
    n = int(input("Nhập số lượng phần tử của danh sách: "))
    
    # Nhập các phần tử của danh sách và sắp xếp danh sách
    lst = []
    for i in range(n):
        value = int(input(f"Nhập phần tử thứ {i + 1}: "))
        lst.append(value)
    
    lst.sort()  # Sắp xếp danh sách theo thứ tự tăng dần
    
    # Nhập phần tử cần tìm kiếm
    item = int(input("Nhập phần tử cần tìm: "))
    
    # Gọi hàm binary_search
    found = binary_search.binary_search(lst, item)
    
    # In kết quả tìm kiếm
    if found:
        print(f"Phần tử {item} có trong danh sách.")
    else:
        print(f"Phần tử {item} không có trong danh sách.")

if __name__ == "__main__":
    main()
