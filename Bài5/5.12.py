print("Sinh vien:Van Tuan Dat")
print("MSSV:235752021610083")
##################



import numpy as np

def main():
    # Giả sử chúng ta có danh sách ID sinh viên và chiều cao
    student_ids = np.array([101, 102, 103, 104, 105])
    heights = np.array([1.75, 1.80, 1.60, 1.65, 1.70])

    # Sử dụng lexsort để sắp xếp theo chiều cao và lấy chỉ số sắp xếp
    # lexsort(arrays) nhận một tuple các mảng cần sắp xếp
    sorted_indices = np.lexsort((student_ids, heights))

    # In ra các chỉ số của thứ tự sắp xếp
    print("Chỉ số của thứ tự sắp xếp:", sorted_indices)

    # Sắp xếp id và chiều cao theo thứ tự của chỉ số đã tính được
    sorted_ids = student_ids[sorted_indices]
    sorted_heights = heights[sorted_indices]

    # In kết quả đã sắp xếp
    print("\nID sinh viên sau khi sắp xếp theo chiều cao:")
    print(sorted_ids)
    print("\nChiều cao của sinh viên sau khi sắp xếp:")
    print(sorted_heights)

if __name__ == "__main__":
    main()
