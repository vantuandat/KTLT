print("Sinh vien:Van Tuan DAt")
print("MSSV: 235752021610083")
###################



# Đểm số dòng trong tếp văn bản

file_name = "file.txt"

try:
    #Mở tệp để đọc
    with open (file_name, 'r', encoding='utf-8') as file:
        # Đếm số dòng bằng cách duyệt qua từng dòng trong tệp
        num_lines = sum (1 for line in file)


        # In số dòng trong tệp 
        print (f"Số dòng trong tệp: {num_lines}")

except FileNotFoundError:
    print (f"Không tìm thấy tệp {file_name} .")
except Exception as e:
    print (f"Đã xảy ra lỗi: {e}")

