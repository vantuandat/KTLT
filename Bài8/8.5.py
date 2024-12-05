print("Sinh vien:Van Tuan Dat")
print("MSSV:235752021610083")
##################

import tkinter as tk

# Hàm xử lý sự kiện khi chọn radio button
def show_selection():
    selected_value = var.get()  # Lấy giá trị của radio button được chọn
    label.config(text=f"Bạn đã chọn: {selected_value}")  # Hiển thị lựa chọn

# Tạo cửa sổ chính
window = tk.Tk()

# Đặt tiêu đề cho cửa sổ
window.title("Cửa sổ với Radio Buttons")

# Đặt kích thước cho cửa sổ
window.geometry("400x300")

# Tạo một biến để lưu giá trị của lựa chọn radio button
var = tk.StringVar()

# Tạo các radio button
radio1 = tk.Radiobutton(window, text="Lựa chọn 1", variable=var, value="Lựa chọn 1", command=show_selection)
radio2 = tk.Radiobutton(window, text="Lựa chọn 2", variable=var, value="Lựa chọn 2", command=show_selection)
radio3 = tk.Radiobutton(window, text="Lựa chọn 3", variable=var, value="Lựa chọn 3", command=show_selection)

# Đặt vị trí cho các radio button
radio1.pack()
radio2.pack()
radio3.pack()

# Thêm một Label để hiển thị lựa chọn của người dùng
label = tk.Label(window, text="Chưa chọn lựa chọn nào", font=("Arial", 12))
label.pack(pady=20)

# Hiển thị cửa sổ
window.mainloop()
