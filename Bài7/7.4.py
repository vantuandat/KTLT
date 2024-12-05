print("Sinh vien:Van Tuan DAt")
print("MSSV: 235752021610083")
###################





# Đọc n dòng đầu tiên của tệp văn bản

file_name = "file.txt"  
n = 1  # Số dòng cần đọc, có thể thay đổi giá trị của n theo nhu cầu

try:
    # Mở tệp để đọc
    with open(file_name, 'r', encoding='utf-8') as file:
        # Đọc n dòng đầu tiên
        for i in range(n):
            line = file.readline()
            if not line:  # Kiểm tra nếu hết tệp
                break
            print(line, end="")  # In dòng ra màn hình, end="" để không thêm dòng trống

except FileNotFoundError:
    print(f"Không tìm thấy tệp {file_name}.")
except Exception as e:
    print(f"Đã xảy ra lỗi: {e}")
