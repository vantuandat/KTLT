print("Sinh vien:Van Tuan DAt")
print("MSSV: 235752021610083")
###################


# Sao chép tệp nhị phân (ví dụ sao chép hình ảnh)

source_file = "file.txt"  # Tệp nguồn (hình ảnh)
destination_file = "copy_image.png"  # Tệp đích

try:
    # Mở tệp nguồn ở chế độ nhị phân để đọc
    with open(source_file, 'rb') as src_file:
        # Đọc toàn bộ nội dung của tệp nguồn
        content = src_file.read()
    
    # Mở tệp đích ở chế độ nhị phân để ghi
    with open(destination_file, 'wb') as dest_file:
        # Ghi nội dung vào tệp đích
        dest_file.write(content)

    print(f"Đã sao chép tệp từ {source_file} vào {destination_file}.")

except FileNotFoundError:
    print(f"Không tìm thấy tệp nguồn {source_file}.")
except Exception as e:
    print(f"Đã xảy ra lỗi: {e}")
