print("Sinh vien:Van Tuan Dat")
print("MSSV:235752021610083")
##################

class ATM:
    def __init__(self, balance=0):
        self.balance = balance  # Khởi tạo số dư, mặc định là 0
        
    def check_balance(self):
        print(f"Số dư hiện tại là: {self.balance} VND")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Số dư không đủ để rút!")
        else:
            self.balance -= amount
            print(f"Đã rút {amount} VND. Số dư còn lại: {self.balance} VND")
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Đã gửi {amount} VND. Số dư hiện tại: {self.balance} VND")

def atm_menu():
    # Tạo đối tượng ATM với số dư ban đầu là 1000 VND
    atm = ATM(1000)

    while True:
        print("\n----- Menu ATM -----")
        print("1. Kiểm tra số dư")
        print("2. Rút tiền")
        print("3. Gửi tiền")
        print("4. Thoát")

         # Nhận lựa chọn của người dùng
        choice = input("Chọn một chức năng (1/2/3/4): ")

        if choice == '1':
            atm.check_balance()  # Kiểm tra số dư
        elif choice == '2':
            try:
                amount = float(input("Nhập số tiền cần rút: "))
                atm.withdraw(amount)  # Rút tiền
            except ValueError:
                print("Vui lòng nhập số tiền hợp lệ!")
        elif choice == '3':
            try:
                amount = float(input("Nhập số tiền cần gửi: "))
                atm.deposit(amount)  # Gửi tiền
            except ValueError:
                print("Vui lòng nhập số tiền hợp lệ!")
        elif choice == '4':
            print("Cảm ơn bạn đã sử dụng dịch vụ ATM!")
            break  # Thoát khỏi vòng lặp và kết thúc chương trình
        else:
            print("Lựa chọn không hợp lệ! Vui lòng thử lại.")

# Chạy menu ATM
atm_menu()
