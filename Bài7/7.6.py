print("Sinh vien:Van Tuan DAt")
print("MSSV: 235752021610083")
###################



# Nối văn bản vào tệp và hiển thị văn bản trong tệp

file_name = "file.txt"
text_to_append = "ban thay the nao"  # Văn bản muốn nối vào tệp
try:
    # Mở tệp ở chế độ append ('a') để thêm văn bản vào cuối tệp
    with open(file_name, 'a', encoding='utf-8') as file:
        # Nối văn bản vào tệp
        file.write(text_to_append)
    
    # Mở tệp lại để đọc và hiển thị nội dung hiện tại
    with open(file_name, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # In nội dung tệp
    print("Nội dung tệp sau khi nối văn bản:")
    print(content)

except FileNotFoundError:
    print(f"Không tìm thấy tệp {file_name}.")
except Exception as e:
    print(f"Đã xảy ra lỗi: {e}")
