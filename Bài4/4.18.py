print("Sinh vien:Van Tuan DAt")
print("MSSV: 235752021610083")
###################

n = int(input("Nhập số nguyên n: "))

# Khởi tạo danh sách Fibonacci
fibonacci = [0, 1]

# Sinh các số Fibonacci nhỏ hơn n
while True:
    next_fib = fibonacci[-1] + fibonacci[-2]  # Tính số Fibonacci tiếp theo
    if next_fib >= n:  # Dừng lại nếu số Fibonacci tiếp theo lớn hơn hoặc bằng n
        break
    fibonacci.append(next_fib)

# In ra danh sách các số Fibonacci nhỏ hơn n
print(fibonacci)

