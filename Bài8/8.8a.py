print("Sinh vien:Van Tuan DAt")
print("MSSV: 235752021610083")
###################


import tkinter as tk

# Hàm hiển thị thông tin cá nhân
def show_info():
    # Cửa sổ mới để hiển thị thông tin cá nhân
    personal_info_window = tk.Toplevel(root)
    personal_info_window.title("Thông tin cá nhân")
    
    # Nhãn hiển thị thông tin cá nhân
    name_label = tk.Label(personal_info_window, text="Họ và tên: Van Tuan Dat")
    name_label.pack(pady=5)
    
    birth_date_label = tk.Label(personal_info_window, text="Ngày sinh: 15/06/2005")
    birth_date_label.pack(pady=5)
    
    mssv_label = tk.Label(personal_info_window, text="MSSV: 235752021610083")
    mssv_label.pack(pady=5)
    
    major_label = tk.Label(personal_info_window, text="Ngành học: Tu dong hoa")
    major_label.pack(pady=5)

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Form Thông tin Cá nhân")

# Nút hiển thị thông tin cá nhân
info_button = tk.Button(root, text="Hiển thị Thông tin Cá nhân", command=show_info)
info_button.pack(pady=10)

# Khởi động ứng dụng
root.mainloop()
