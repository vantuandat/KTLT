print("Sinh vien:Van Tuan DAt")
print("MSSV: 235752021610083")
###################

def tach_ho_ten(ten_day_du):
  """Ham tach ho va ten rieng

  Args:
    ten_day_du: ten day du cua nguoi

  Returns:
    Mot tuple gom ho va ten rieng
  """
  ho, ten = ten_day_du.split(maxsplit=1)

  return ho, ten

ten = input("nhap ten day du: ")
ho,ten = tach_ho_ten(ten)
print("Ho:", ho)
print("Ten:", ten)
