print("Sinh vien:Van Tuan DAt")
print("MSSV: 235752021610083")
###################



# Nhập chuỗi từ bàn phím
input_string = input("Nhập một chuỗi: ")

# Loại bỏ tất cả các chữ số khỏi chuỗi
output_string = ''.join([char for char in input_string if not char.isdigit()])

# In chuỗi mới
print("Chuỗi sau khi loại bỏ chữ số:", output_string)
