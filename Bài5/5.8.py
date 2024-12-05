print("Sinh vien:Van Tuan DAt")
print("MSSV: 235752021610083")
###################


# main.py

# Nhập danh sách từ bàn phím
n = int(input("Nhập số lượng phần tử của danh sách: "))
dlist = []

for i in range(n):
    element = int(input(f"Nhập phần tử thứ {i+1}: "))
    dlist.append(element)

# Nhập phần tử cần tìm
item = int(input("Nhập phần tử cần tìm: "))

# Tìm kiếm phần tử trong danh sách
from sequential_search import Sequential_Search

result = Sequential_Search(dlist, item)

if result[0]:
    print(f"Phần tử {item} tìm thấy tại chỉ số {result[1]}")
else:
    print(f"Phần tử {item} không có trong danh sách.")
