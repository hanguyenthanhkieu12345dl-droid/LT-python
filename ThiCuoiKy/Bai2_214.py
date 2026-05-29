import math

# Hàm kiểm tra số nguyên tố
def la_so_nguyen_to(n):
    if n < 2:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True

# Nhập số nguyên dương n

n = int(input("Nhập số nguyên dương n: "))

# 1. Kiểm tra n có phải số nguyên tố hay không
if la_so_nguyen_to(n):
    print(n, "là số nguyên tố")
else:
    print(n, "không phải là số nguyên tố")

# 2. Đếm các số nguyên tố nhỏ hơn n
dem = 0

for i in range(2, n):
    if la_so_nguyen_to(i):
        dem += 1

print("Có", dem, "số nguyên tố nhỏ hơn", n)

# 3. Liệt kê các ước số nguyên tố của n
print("Các ước số nguyên tố của", n, "là:")

for i in range(1, n + 1):
    if n % i == 0 and la_so_nguyen_to(i):
        print(i, end=" ")