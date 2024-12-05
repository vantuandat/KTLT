print("Sinh vien:Van Tuan Dat")
print("MSSV:235752021610083")
##################

import tkinter as tk

# Hàm xử lý sự kiện khi nhấn nút
def on_button_click():
    print("Nút đã được nhấn!")

# Tạo cửa sổ chính
window = tk.Tk()

# Đặt tiêu đề cho cửa sổ
window.title("Cửa sổ với Button màu sắc")

# Đặt kích thước cho cửa sổ
window.geometry("400x300")

# Thêm một Button vào cửa sổ với màu nền và màu chữ
button = tk.Button(window, 
                   text="Nhấn vào đây",  # Nội dung của nút
                   command=on_button_click,  # Xử lý khi nhấn nút
                   bg="blue",  # Màu nền của nút
                   fg="white",  # Màu chữ của nút
                   font=("Arial", 14))  # Thay đổi font chữ của nút

# Đặt vị trí cho Button (Sử dụng pack để canh giữa)
button.pack(pady=50)  # pady là khoảng cách dọc trên và dưới của button

# Hiển thị cửa sổ
window.mainloop()
