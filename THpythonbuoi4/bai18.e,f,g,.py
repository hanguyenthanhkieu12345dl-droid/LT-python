import math

# e) Số phong phú
so_phong_phu = lambda n: sum(i for i in range(1, n) if n % i == 0) > n

# f) Số tăng dần
so_tang_dan = lambda n: all(str(n)[i] <= str(n)[i+1] for i in range(len(str(n)) - 1))

# g) Số Armstrong
so_armstrong = lambda n: sum(int(ch) ** len(str(n)) for ch in str(n)) == n

# ---------------- KẾT QUẢ ----------------

print("e) Các số phong phú từ 1 đến 100:")
for i in range(1, 101):
    if so_phong_phu(i):
        print(i, end=" ")

print("\n\nf) Các số tăng dần từ 1 đến 200:")
for i in range(1, 201):
    if so_tang_dan(i):
        print(i, end=" ")

print("\n\ng) Các số Armstrong từ 1 đến 1 triệu:")
for i in range(1, 1000001):
    if so_armstrong(i):
        print(i, end=" ")