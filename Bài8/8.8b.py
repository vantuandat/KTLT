print("Sinh vien:Van Tuan DAt")
print("MSSV: 235752021610083")
###################


import tkinter as tk

# Phần a: Hiển thị thông tin cá nhân
def show_info():
    # Cửa sổ mới để hiển thị thông tin cá nhân
    personal_info_window = tk.Toplevel(root)
    personal_info_window.title("Thông tin cá nhân")

    # Các nhãn hiển thị thông tin cá nhân
    name_label = tk.Label(personal_info_window, text="Họ và tên: Nguyễn Văn A")
    name_label.pack(pady=5)

    birth_date_label = tk.Label(personal_info_window, text="Ngày sinh: 15/06/2005")
    birth_date_label.pack(pady=5)

    mssv_label = tk.Label(personal_info_window, text="MSSV: 235752021610083")
    mssv_label.pack(pady=5)

    major_label = tk.Label(personal_info_window, text="Ngành học: Tu Dong Hoa")
    major_label.pack(pady=5)

# Phần b: Hiển thị lựa chọn của radio button
def show_selected_option():
    selected_option = radio_var.get()  # Lấy giá trị của radio button được chọn
    result_label.config(text=f"Số bạn chọn là: {selected_option}")

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Form Thông tin Cá nhân và Radio Button")

# Nút hiển thị thông tin cá nhân
info_button = tk.Button(root, text="Hiển thị Thông tin Cá nhân", command=show_info)
info_button.pack(pady=10)

# Phần radio buttons
radio_var = tk.IntVar()  # Biến để lưu giá trị của radio button

radio_button_1 = tk.Radiobutton(root, text="1", variable=radio_var, value=1)
radio_button_1.pack()

radio_button_2 = tk.Radiobutton(root, text="2", variable=radio_var, value=2)
radio_button_2.pack()

radio_button_3 = tk.Radiobutton(root, text="3", variable=radio_var, value=3)
radio_button_3.pack()

# Thêm nút "Click Me" để hiển thị lựa chọn
click_me_button = tk.Button(root, text="Click Me", command=show_selected_option)
click_me_button.pack(pady=10)

# Nhãn để hiển thị kết quả lựa chọn
result_label = tk.Label(root, text="Số bạn chọn là: ")
result_label.pack(pady=10)

# Khởi động ứng dụng
root.mainloop()
