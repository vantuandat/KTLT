print("Sinh vien:Van Tuan DAt")
print("MSSV: 235752021610083")
###################



def benefit(t, n, k):
    # Tính số tiền sau k tháng với lãi suất kép
    A = n * (1 + t / 100) ** k
    return A

# Nhập các giá trị từ người dùng
t = float(input("Nhập lãi suất hàng tháng (t%): "))
n = float(input("Nhập số vốn ban đầu (n): "))
k = int(input("Nhập số tháng gửi (k): "))

# Tính và in kết quả
result = benefit(t, n, k)
print(f"Số tiền nhận được sau {k} tháng là: {result:.2f}")

