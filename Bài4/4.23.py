print("Sinh vien:Van Tuan DAt")
print("MSSV: 235752021610083")
###################




# Nhập câu từ người dùng
sentence = input("Nhập một câu: ")

# Khởi tạo biến đếm chữ cái và chữ số
letter_count = 0
digit_count = 0

# Duyệt qua từng ký tự trong câu
for char in sentence:
    if char.isalpha():  # Kiểm tra nếu ký tự là chữ cái
        letter_count += 1
    elif char.isdigit():  # Kiểm tra nếu ký tự là chữ số
        digit_count += 1

# In kết quả
print(f"Số chữ cái trong câu: {letter_count}")
print(f"Số chữ số trong câu: {digit_count}")
