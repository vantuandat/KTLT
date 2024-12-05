print("Sinh vien:Van Tuan DAt")
print("MSSV: 235752021610083")
###################


print("Giai phuong trinh bac 2: ax2 + bx + c = 0 (a, b khac 0)")
print("==========")
a = float(input("Moi ban nhap he so a: "))
while True:
    if a == 0:
        a = float(input("So a phai khac 0. Moi ban nhap lai so a:"))
    else:
        break

b = float(input("Moi ban nhap he so b:"))
while True:
    if b == 0:
        b = float(input("So b phai khac 0. Moi nhap lai so b:"))
    else:
        break
c = float(input("Moi ban nhap he so c: "))
delta = b**2 - 4 * a * c
if delta < 0:
    print("Phuong trinh vo nghiem")
elif delta == 0:
    print("Phuong trinh co nghiem kep x1 = x2 =", -(b/ (2 * a)) )
else:
    print("Phuong trinh co hai nghiem phan biet:")
    print("x1 = ", (-(b) + math.sqrt(delta))/(2*a) )
    print("x2 = ", (-(b) - math.sqrt(delat))/(2*a) )
    
