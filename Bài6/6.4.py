print("Sinh vien:Van Tuan Dat")
print("MSSV:235752021610083")
##################




class RomanToInteger:
    def __init__(self):
        # Tạo một dictionary để ánh xạ các ký tự La Mã tới giá trị số nguyên
        self.roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
    
    def convert(self, roman):
        # Biến để lưu trữ giá trị số nguyên
        total = 0
        # Duyệt qua từng ký tự trong chuỗi La Mã
        for i in range(len(roman)):
            # Lấy giá trị của ký tự hiện tại và ký tự kế tiếp
            current_value = self.roman_map[roman[i]]
            # Kiểm tra nếu ký tự hiện tại có giá trị nhỏ hơn ký tự kế tiếp
            if i + 1 < len(roman) and current_value < self.roman_map[roman[i + 1]]:
                total -= current_value  # Trừ giá trị của ký tự hiện tại
            else:
                total += current_value  # Cộng giá trị của ký tự hiện tại
        return total

# Tạo đối tượng RomanToInteger và chuyển đổi số La Mã
roman_to_integer = RomanToInteger()

# Nhập số La Mã từ bàn phím
roman_number = input("Nhập số La Mã: ")

# Chuyển đổi và in kết quả
print(f"Số nguyên tương ứng với số La Mã '{roman_number}' là: {roman_to_integer.convert(roman_number)}")

