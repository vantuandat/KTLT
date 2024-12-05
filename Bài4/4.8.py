print("Sinh vien:Van Tuan DAt")
print("MSSV: 235752021610083")
###################

# Nhập dãy các từ từ bàn phím
input_string = input("Nhập một dãy các từ (cách nhau bởi dấu cách): ")

# Tách chuỗi thành danh sách các từ
words = input_string.split()

# Tìm độ dài của từ dài nhất
max_length = max(len(word) for word in words)

# Lọc ra các từ có độ dài bằng độ dài của từ dài nhất
longest_words = [word for word in words if len(word) == max_length]

# In ra các từ dài nhất
print("Các từ dài nhất trong dãy là:")
for word in longest_words:
    print(word)
