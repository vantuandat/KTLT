print("Sinh vien:Van Tuan DAt")
print("MSSV: 235752021610083")
###################



# Nhập danh sách các số từ người dùng (các số được cách nhau bằng dấu phẩy)
user_input = input("Nhập danh sách các số (các số cách nhau bằng dấu phẩy): ")

# Chuyển chuỗi nhập vào thành danh sách các số nguyên
numbers = [int(num) for num in user_input.split(',')]

# Lọc các số lẻ từ danh sách
odd_numbers = [num for num in numbers if num % 2 != 0]

# In kết quả
print("Danh sách các số lẻ:", odd_numbers)
