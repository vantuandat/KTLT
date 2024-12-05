print("Sinh vien:Van Tuan DAt")
print("MSSV: 235752021610083")
###################



# Tìm những từ dài nhất trong văn bản

file_name = "file.txt"  

try:
    # Mở tệp để đọc
    with open(file_name, 'r', encoding='utf-8') as file:
        # Đọc toàn bộ nội dung của tệp
        text = file.read()
    
    # Tách văn bản thành các từ (bằng cách sử dụng split)
    words = text.split()

    # Tìm độ dài của từ dài nhất
    max_length = max(len(word) for word in words)

    # Tìm những từ có độ dài bằng với độ dài lớn nhất
    longest_words = [word for word in words if len(word) == max_length]

    # In những từ dài nhất và độ dài của chúng
    print(f"Các từ dài nhất ({max_length} ký tự) là:")
    for word in longest_words:
        print(word)

except FileNotFoundError:
    print(f"Không tìm thấy tệp {file_name}.")
except Exception as e:
    print(f"Đã xảy ra lỗi: {e}")

