print("Sinh vien:Van Tuan DAt")
print("MSSV: 235752021610083")
###################

# Đọc n dòng cuối cùng của tệp văn bản

file_name = "file.txt"  
n = 2  # Số dòng cuối cùng cần đọc, có thể thay đổi giá trị của n theo nhu cầu

try:
    # Mở tệp để đọc
    with open(file_name, 'r', encoding='utf-8') as file:
        # Đọc tất cả các dòng trong tệp
        lines = file.readlines()
    
    # Kiểm tra nếu số dòng trong tệp ít hơn n
    if len(lines) < n:
        print("Tệp có ít hơn n dòng.")
        n = len(lines)  # Đọc tất cả các dòng nếu số dòng trong tệp ít hơn n
    
    # In n dòng cuối cùng của tệp
    print(f"{n} dòng cuối cùng của tệp là:")
    for line in lines[-n:]:
        print(line, end="")  # In dòng ra màn hình, không thêm dòng trống

except FileNotFoundError:
    print(f"Không tìm thấy tệp {file_name}.")
except Exception as e:
    print(f"Đã xảy ra lỗi: {e}")

