print("Sinh vien:Van Tuan DAt")
print("MSSV: 235752021610083")
###################

# Viết nội dung danh sách vào tệp

file_name = "file.txt"  # Tên tệp bạn muốn ghi vào
my_list = ["Dòng 1", "Dòng 2", "Dòng 3", "Dòng 4"]  # Danh sách cần ghi vào tệp

try:
    # Mở tệp để ghi (chế độ 'w' sẽ tạo tệp mới hoặc ghi đè lên tệp cũ)
    with open(file_name, 'w', encoding='utf-8') as file:
        # Ghi từng phần tử của danh sách vào tệp, mỗi phần tử một dòng
        for item in my_list:
            file.write(item + '\n')  # Thêm ký tự xuống dòng sau mỗi phần tử

    print(f"Đã ghi nội dung danh sách vào tệp {file_name}.")

except Exception as e:
    print(f"Đã xảy ra lỗi: {e}")

