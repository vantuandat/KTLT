print("Sinh vien:Van Tuan DAt")
print("MSSV: 235752021610083")
###################

# Hàm tìm các số nguyên tố nhỏ hơn n bằng thuật toán Sieve of Eratosthenes
def sieve_of_eratosthenes(limit):
    # Khởi tạo một mảng đánh dấu tất cả các số là số nguyên tố (True)
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False  # 0 và 1 không phải là số nguyên tố

    for start in range(2, int(limit ** 0.5) + 1):
        if sieve[start]:  # Nếu start là số nguyên tố
            for i in range(start * start, limit + 1, start):
                sieve[i] = False  # Đánh dấu các bội số của start là không phải số nguyên tố

    # Trả về một danh sách các số nguyên tố
    return [num for num, is_prime in enumerate(sieve) if is_prime]

# Tạo tuple P chứa các số nguyên tố nhỏ hơn 1 triệu
primes = sieve_of_eratosthenes(1000000)
P = tuple(primes)

# In kết quả
print(P[:20])  # In ra 20 phần tử đầu tiên để kiểm tra
print(f"Tổng số lượng số nguyên tố nhỏ hơn 1 triệu: {len(P)}")

