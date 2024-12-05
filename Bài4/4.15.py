print("Sinh vien:Van Tuan DAt")
print("MSSV: 235752021610083")
###################



# Nhập chuỗi các từ từ người dùng
input_string = input("Nhập chuỗi các từ tiếng Anh, cách nhau bởi dấu cách: ")

# Tách chuỗi thành danh sách các từ
words = input_string.split()

# Sắp xếp các từ theo thứ tự từ điển
sorted_words = sorted(words)

# In ra các từ theo thứ tự từ điển
print("Các từ theo thứ tự từ điển là:",','.join(sorted_words))
