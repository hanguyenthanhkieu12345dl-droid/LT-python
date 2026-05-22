import math

# a) Số thân thiện
so_than_thien = lambda n: math.gcd(n, int(str(n)[::-1])) == 1

# b) Số chính phương
so_chinh_phuong = lambda n: int(math.sqrt(n)) ** 2 == n

# c1) Số đồng nhất dùng all
so_dong_nhat_all = lambda k: k > 0 and all(ch == str(k)[0] for ch in str(k))

# c2) Số đồng nhất dùng any
so_dong_nhat_any = lambda k: k > 0 and not any(ch != str(k)[0] for ch in str(k))

# d) Số hoàn thiện
so_hoan_thien = lambda n: n > 1 and sum(i for i in range(1, n) if n % i == 0) == n

# ---------------- KẾT QUẢ ----------------

print("a) Các số thân thiện từ 1 đến 100:")
for i in range(1, 101):
    if so_than_thien(i):
        print(i, end=" ")

print("\n\nb) Các số chính phương từ 1 đến 100:")
for i in range(1, 101):
    if so_chinh_phuong(i):
        print(i, end=" ")

print("\n\nc1) Các số đồng nhất (dùng all) từ 1 đến 1000:")
for i in range(1, 1001):
    if so_dong_nhat_all(i):
        print(i, end=" ")

print("\n\nc2) Các số đồng nhất (dùng any) từ 1 đến 1000:")
for i in range(1, 1001):
    if so_dong_nhat_any(i):
        print(i, end=" ")

print("\n\nd) Các số hoàn thiện từ 1 đến 10000:")
for i in range(1, 10001):
    if so_hoan_thien(i):
        print(i, end=" ")