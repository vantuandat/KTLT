print("Sinh vien:Van Tuan DAt")
print("MSSV: 235752021610083")
###################



# Nhập số dư ban đầu
balance = float(input("Nhập số dư ban đầu của tài khoản: "))

# Nhập số lượng giao dịch
num_transactions = int(input("Nhập số lượng giao dịch: "))

# Duyệt qua các giao dịch
for i in range(num_transactions):
    # Nhập một giao dịch (có thể là số âm hoặc dương)
    transaction = float(input(f"Nhập giao dịch thứ {i+1} (số dương là gửi tiền, số âm là rút tiền): "))
    
    # Cập nhật số dư
    balance += transaction

# In ra số dư cuối cùng
print(f"Số dư cuối cùng của tài khoản là: {balance:.2f}")

