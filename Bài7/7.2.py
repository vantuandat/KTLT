print("Sinh vien:Van Tuan DAt")
print("MSSV: 235752021610083")
###################



# Đọc file và tính số ký tự, số từ, số dòng

file_name = "file.txt"  # Thay 'your_file.txt' bằng tên file bạn muốn đọc

try:
    # Khởi tạo các biến đếm
    num_lines = 0
    num_words = 0
    num_chars = 0

    # Mở file để đọc
    with open(file_name, 'r', encoding='utf-8') as file:
        # Duyệt qua từng dòng trong file
        for line in file:
            num_lines += 1  # Tăng số dòng
            num_chars += len(line)  # Tính số ký tự trong dòng
            num_words += len(line.split())  # Tính số từ trong dòng (sử dụng split để tách từ)

    # In kết quả
    print(f"Số dòng: {num_lines}")
    print(f"Số từ: {num_words}")
    print(f"Số ký tự: {num_chars}")

except FileNotFoundError:
    print(f"File {file_name} không tồn tại.")
except Exception as e:
    print(f"Đã xảy ra lỗi: {e}")
