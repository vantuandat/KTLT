print("Sinh vien:Van Tuan Dat")
print("MSSV:235752021610083")
##################

import numpy as np

def main():
    # Tạo một mảng có cấu trúc chứa thông tin sinh viên
    # Mảng có các trường: tên (string), chiều cao (float), lớp (int)
    student_dtype = np.dtype([('name', 'U20'), ('height', 'f4'), ('class', 'i4')])
    
    # Nhập thông tin của sinh viên
    n = int(input("Nhập số lượng sinh viên: "))
    students = []

    for i in range(n):
        name = input(f"Nhập tên sinh viên thứ {i + 1}: ")
        height = float(input(f"Nhập chiều cao sinh viên thứ {i + 1} (m): "))
        student_class = int(input(f"Nhập lớp của sinh viên thứ {i + 1}: "))
        students.append((name, height, student_class))

    # Chuyển danh sách sinh viên thành mảng có cấu trúc
    students_array = np.array(students, dtype=student_dtype)

    # In ra mảng sinh viên trước khi sắp xếp
    print("\nDanh sách sinh viên trước khi sắp xếp:")
    print(students_array)

    # Sắp xếp mảng: đầu tiên theo lớp, sau đó theo chiều cao nếu lớp bằng nhau
    sorted_students = np.sort(students_array, order=['class', 'height'])

    # In ra mảng sinh viên sau khi sắp xếp
    print("\nDanh sách sinh viên sau khi sắp xếp theo lớp và chiều cao:")
    print(sorted_students)

if __name__ == "__main__":
    main()
