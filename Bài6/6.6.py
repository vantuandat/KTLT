print("Sinh vien:Van Tuan Dat")
print("MSSV:235752021610083")
##################



class StringManipulator:
    def __init__(self):
        self.input_string = ""
    
    def get_String(self):
        # Nhận chuỗi từ người dùng
        self.input_string = input("Nhập chuỗi: ")
    
    def print_String(self):
        # In chuỗi dưới dạng chữ in hoa
        print(self.input_string.upper())

# Tạo đối tượng StringManipulator
string_obj = StringManipulator()

# Gọi phương thức get_String để nhận chuỗi
string_obj.get_String()

# Gọi phương thức print_String để in chuỗi in hoa
string_obj.print_String()
