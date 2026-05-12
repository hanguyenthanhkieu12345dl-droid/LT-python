# Danh sách các loại tiền
tien = [500, 200, 100, 50, 20, 10, 5, 2, 1]

# Nhập số tiền X
x = int(input("Nhập số tiền X: "))

tong_to = 0

print(f"\nSố tiền {x} được đổi thành:")

# Đổi tiền
for loai in tien:
    so_to = x // loai
    x = x % loai
    
    print(f"Loại {loai} gồm {so_to} tờ")
    
    tong_to += so_to

print(f"TỔNG CỘNG CÓ {tong_to} TỜ")