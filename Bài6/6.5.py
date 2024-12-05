print("Sinh vien:Van Tuan Dat")
print("MSSV:235752021610083")
##################





class ReverseWords:
    def __init__(self):
        pass
    
    def reverse_words(self, input_string):
        # Tách chuỗi thành các từ
        words = input_string.split()
        
        # Đảo ngược từng từ trong danh sách
        reversed_words = [word[::-1] for word in words]
        
        # Nối các từ đã đảo ngược lại thành chuỗi
        result = ' '.join(reversed_words)
        
        return result

# Tạo đối tượng ReverseWords
reverse_obj = ReverseWords()

# Nhập chuỗi từ người dùng
input_string = input("Nhập chuỗi: ")

# Đảo ngược chuỗi từ từng chữ
reversed_string = reverse_obj.reverse_words(input_string)

# In kết quả
print("Chuỗi đã đảo ngược từ từng chữ:", reversed_string)
