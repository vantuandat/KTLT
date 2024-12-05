print("Sinh vien:Van Tuan DAt")
print("MSSV: 235752021610083")
###################




# Hàm kiểm tra xem tất cả các chữ số trong số có phải là số chẵn không
def all_even_digits(num):
    return all(int(digit) % 2 == 0 for digit in str(num))

# Tìm các số có tất cả các chữ số là số chẵn trong đoạn 1000 đến 3000
result = [str(num) for num in range(1000, 3001) if all_even_digits(num)]

# In các số tìm được thành chuỗi phân tách bằng dấu phẩy
print(','.join(result))
