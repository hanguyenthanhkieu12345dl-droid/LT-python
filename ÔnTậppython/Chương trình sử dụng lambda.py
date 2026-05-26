import math

# 1. Trị tuyệt đối
tri_tuyet_doi = lambda n: abs(n)

# 2. n + 15
cong_15 = lambda n: n + 15

# 3. Tích của x và y
tich = lambda x, y: x * y

# 4. Kiểm tra bội số của 13 hoặc 19
boi_13_19 = lambda n: n % 13 == 0 or n % 19 == 0

# 5. Diện tích hình tròn
dien_tich_hinh_tron = lambda r: math.pi * r * r

# 6. Chu vi hình chữ nhật
chu_vi_hcn = lambda d, r: (d + r) * 2

# 7. Kiểm tra số chính phương
so_chinh_phuong = lambda n: int(math.sqrt(n))**2 == n

# 8. Kiểm tra số nguyên tố
so_nguyen_to = lambda n: (
    n >= 2 and
    all(n % i != 0 for i in range(2, int(math.sqrt(n)) + 1))
)

# 9. Kiểm tra tam giác
kiem_tra_tam_giac = lambda a, b, c: (
    "Không phải tam giác"
    if a + b <= c or a + c <= b or b + c <= a
    else "Tam giác đều"
    if a == b == c
    else "Tam giác cân"
    if a == b or a == c or b == c
    else "Tam giác vuông"
    if a*a + b*b == c*c or
       a*a + c*c == b*b or
       b*b + c*c == a*a
    else "Tam giác thường"
)

# TEST

print("1.", tri_tuyet_doi(-9))

print("2.", cong_15(10))

print("3.", tich(4, 5))

print("4.", boi_13_19(39))

print("5. Diện tích hình tròn =", round(dien_tich_hinh_tron(5), 2))

print("6. Chu vi HCN =", chu_vi_hcn(4, 6))

print("7.", so_chinh_phuong(16))

print("8.", so_nguyen_to(17))

print("9.", kiem_tra_tam_giac(3, 4, 5))