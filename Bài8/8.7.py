print("Sinh vien:Van Tuan DAt")
print("MSSV: 235752021610083")
###################


import tkinter as tk
import random

# Danh sách các màu sắc tiếng Anh
colours = ['Red', 'Blue', 'Green', 'Pink', 'Black', 
           'Yellow', 'Orange', 'White', 'Purple', 'Brown']

# Khởi tạo điểm số và thời gian chơi
score = 0
timeleft = 120  # Thời gian chơi là 120 giây

# Hàm bắt đầu trò chơi khi nhấn phím Enter
def startGame(event):
    global timeleft
    if timeleft == 120:  # Chỉ bắt đầu khi thời gian là 120
        countdown()
        nextColour()

# Hàm chọn và hiển thị màu tiếp theo
def nextColour():
    global score, timeleft
    if timeleft > 0:  # Nếu thời gian còn
        e.focus_set()  # Làm cho hộp nhập liệu được chọn
        # Kiểm tra nếu người chơi nhập đúng màu
        if e.get().lower() == colours[1].lower():
            score += 2  # Cộng 2 điểm khi đoán đúng
        else:
            score -= 1  # Trừ 1 điểm khi đoán sai
        e.delete(0, tk.END)  # Xóa nội dung hộp nhập liệu
        random.shuffle(colours)  # Trộn các màu lại
        # Thay đổi màu chữ và màu hiển thị
        label.config(fg=colours[1], text=colours[0])
        scoreLabel.config(text="Score: " + str(score))  # Cập nhật điểm

# Hàm đếm ngược thời gian
def countdown():
    global timeleft
    if timeleft > 0:  # Nếu thời gian còn
        timeleft -= 1
        timeLabel.config(text="Time left: " + str(timeleft))  # Cập nhật thời gian
        timeLabel.after(1000, countdown)  # Tiếp tục gọi hàm sau 1 giây

# Khởi tạo giao diện GUI
root = tk.Tk()

# Cài đặt tiêu đề cho cửa sổ
root.title("COLORGAME")

# Cài đặt kích thước cửa sổ
root.geometry("375x250")

# Thêm nhãn hướng dẫn
instructions = tk.Label(root, text="Type in the colour of the words, and not the word text!",
                        font=('Helvetica', 12))
instructions.pack()

# Thêm nhãn điểm số
scoreLabel = tk.Label(root, text="Press Enter to start", font=('Helvetica', 12))
scoreLabel.pack()

# Thêm nhãn thời gian còn lại
timeLabel = tk.Label(root, text="Time left: " + str(timeleft), font=('Helvetica', 12))
timeLabel.pack()

# Thêm nhãn hiển thị màu sắc
label = tk.Label(root, font=('Helvetica', 60))
label.pack()

# Thêm hộp nhập liệu để người chơi nhập màu
e = tk.Entry(root)

# Khi nhấn phím Enter, gọi hàm startGame
root.bind('<Return>', startGame)
e.pack()

# Đặt focus vào hộp nhập liệu
e.focus_set()

# Chạy giao diện
root.mainloop()

