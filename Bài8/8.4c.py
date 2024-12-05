print("Sinh vien:Van Tuan Dat")
print("MSSV:235752021610083")
##################
import tkinter as tk

# Hàm xử lý sự kiện khi nhấn phím
def key_press(event):
    # In ra ký tự của phím đã nhấn
    print(f"Bạn đã nhấn phím: {event.char}")

# Tạo cửa sổ chính
window = tk.Tk()

# Đặt tiêu đề cho cửa sổ
window.title("Cửa sổ xử lý sự kiện phím bấm")

# Đặt kích thước cho cửa sổ
window.geometry("400x300")

# Thêm một Label hướng dẫn người dùng
label = tk.Label(window, text="Hãy nhấn một phím!", font=("Arial", 14))
label.pack(pady=50)

# Liên kết sự kiện nhấn phím với phương thức xử lý
window.bind("<Key>", key_press)  # Bắt mọi phím nhấn

# Hiển thị cửa sổ
window.mainloop()
