print("Sinh vien:Van Tuan DAt")
print("MSSV: 235752021610083")
###################


def generate_pascals_triangle(n):
    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)
    return triangle

n = int(input("Nhập số n: "))
triangle = generate_pascals_triangle(n)

# In ra n dòng đầu tiên của tam giác Pascal
for row in triangle:
    print(' '.join(map(str, row)))
