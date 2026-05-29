import math

# 1. Hàm lambda kiểm tra số chính phương

so_chinh_phuong = lambda n: math.sqrt(n) == int(math.sqrt(n))

# Nhập số cần kiểm tra
n = int(input("Nhập số nguyên n: "))

if so_chinh_phuong(n):
    print(n, "là số chính phương")
else:
    print(n, "không phải là số chính phương")


# 2. Hàm lambda kiểm tra loại tam giác

# Nhập 3 cạnh
a = int(input("Nhập cạnh a: "))
b = int(input("Nhập cạnh b: "))
c = int(input("Nhập cạnh c: "))

# Kiểm tra tam giác hợp lệ
tam_giac = lambda a, b, c: a + b > c and a + c > b and b + c > a

if tam_giac(a, b, c):

    # Tam giác đều
    if a == b == c:
        print("Đây là tam giác đều")

    # Tam giác vuông cân
    elif (a == b or a == c or b == c) and \
         (a*a + b*b == c*c or
          a*a + c*c == b*b or
          b*b + c*c == a*a):
        print("Đây là tam giác vuông cân")

    # Tam giác vuông
    elif (a*a + b*b == c*c or
          a*a + c*c == b*b or
          b*b + c*c == a*a):
        print("Đây là tam giác vuông")

    # Tam giác cân
    elif a == b or a == c or b == c:
        print("Đây là tam giác cân")

    # Tam giác thường
    else:
        print("Đây là tam giác thường")

else:
    print("Ba cạnh không tạo thành tam giác")