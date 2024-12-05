print("Sinh vien:Van Tuan DAt")
print("MSSV: 235752021610083")
###################



# Đọc và in toàn bộ nội dung của tệp văn bản

file_name = "file.txt"  # Thay 'your_file.txt' bằng tên tệp bạn muốn đọc

try:
    # Mở tệp để đọc
    with open(file_name, 'r', encoding='utf-8') as file:
        # Đọc toàn bộ nội dung của tệp
        content = file.read()
        
    # In nội dung tệp
    print(content)

except FileNotFoundError:
    print(f"Không tìm thấy tệp {file_name}.")
except Exception as e:
    print(f"Đã xảy ra lỗi: {e}")
