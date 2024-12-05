print("Sinh vien:Van Tuan DAt")
print("MSSV: 235752021610083")
###################




# Nhập câu từ người dùng
sentence = input("Nhập một câu: ")

# Khởi tạo biến đếm chữ hoa và chữ thường
upper_count = 0
lower_count = 0

# Duyệt qua từng ký tự trong câu
for char in sentence:
    if char.isupper():  # Kiểm tra nếu ký tự là chữ hoa
        upper_count += 1
    elif char.islower():  # Kiểm tra nếu ký tự là chữ thường
        lower_count += 1

# In kết quả
print(f"Số chữ hoa trong câu: {upper_count}")
print(f"Số chữ thường trong câu: {lower_count}")
