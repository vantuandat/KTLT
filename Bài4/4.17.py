print("Sinh vien:Van Tuan DAt")
print("MSSV: 235752021610083")
###################

# Hàm tính tổng các ước số của một số
def sum_of_divisors(x):
    total = 0
    # Duyệt qua các số từ 1 đến x//2, vì các ước số của x không thể lớn hơn x//2
    for i in range(1, x // 2 + 1):
        if x % i == 0:
            total += i
    return total

# Nhập số nguyên dương n
n = int(input("Nhập số nguyên dương n: "))

# Duyệt qua các số nhỏ hơn n
print(f"Các số nguyên dương nhỏ hơn {n} có tổng các ước số lớn hơn chính nó:")
for i in range(1, n):
    if sum_of_divisors(i) > i:
        print(i)

