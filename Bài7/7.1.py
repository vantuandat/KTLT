print("Sinh vien:Van Tuan DAt")
print("MSSV: 235752021610083")
###################


# Đọc nội dung file và in đảo ngược kết quả

# Mở file để đọc
file_name = "file.txt"  # Thay 'your_file.txt' bằng tên file bạn muốn đọc

try:
    with open(file_name, 'r', encoding='utf-8') as file:
        # Đọc tất cả nội dung của file
        content = file.read()

    # Đảo ngược nội dung
    reversed_content = content[::-1]

    # In kết quả đảo ngược
    print(reversed_content)

except FileNotFoundError:
    print(f"File {file_name} không tồn tại.")
except Exception as e:
    print(f"Đã xảy ra lỗi: {e}")
