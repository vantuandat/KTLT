print("Sinh vien:Van Tuan Dat")
print("MSSV:235752021610083")
##################

# Class cơ sở
class Nguoi:
    def getGender(self):
        return "Giới tính chưa xác định"

# Class con Nam kế thừa từ Nguoi
class Nam(Nguoi):
    def getGender(self):
        return "Nam"

# Class con Nu kế thừa từ Nguoi
class Nu(Nguoi):
    def getGender(self):
        return "Nữ"

# Tạo đối tượng của các lớp và gọi phương thức getGender
nam = Nam()
nu = Nu()

# In giới tính của đối tượng
print(nam.getGender())  # Output: Nam
print(nu.getGender())   # Output: Nữ
