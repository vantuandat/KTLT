print("Sinh vien:Van Tuan DAt")
print("MSSV: 235752021610083")
###################



import math

# Khởi tạo vị trí ban đầu của robot
pos = [0, 0]

# Nhập các chỉ thị di chuyển từ người dùng
while True:
    s = input("Nhập hướng và số bước (hoặc nhấn Enter để kết thúc): ")
    if not s:
        break  # Dừng nếu không có dữ liệu đầu vào
    movement = s.split(" ")
    direction = movement[0]
    steps = int(movement[1])

    # Cập nhật vị trí của robot theo hướng di chuyển
    if direction == "UP":
        pos[0] += steps
    elif direction == "DOWN":
        pos[0] -= steps
    elif direction == "LEFT":
        pos[1] -= steps
    elif direction == "RIGHT":
        pos[1] += steps
    else:
        pass  # Không làm gì nếu hướng không hợp lệ

# Tính toán và in khoảng cách từ vị trí hiện tại về vị trí ban đầu (0, 0)
distance = math.sqrt(pos[0]**2 + pos[1]**2)
print(int(round(distance)))  # In khoảng cách làm số nguyên gần nhất
