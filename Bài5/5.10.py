print("Sinh vien:Van Tuan Dat")
print("MSSV:235752021610083")
##################


# main.py
import bubbleSort  # Nhập module bubbleSort

def main():
    # Nhập số lượng phần tử của danh sách
    n = int(input("Nhập số lượng phần tử của danh sách: "))
    
    # Nhập các phần tử của danh sách
    nlist = []
    for i in range(n):
        value = int(input(f"Nhập phần tử thứ {i + 1}: "))
        nlist.append(value)
    
    # Gọi hàm bubbleSort để sắp xếp danh sách
    bubbleSort.bubbleSort(nlist)
    
    # In kết quả sau khi sắp xếp
    print(f"Danh sách sau khi sắp xếp: {nlist}")

if __name__ == "__main__":
    main()
