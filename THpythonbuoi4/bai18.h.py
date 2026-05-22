import math

# Cách 1: Đếm số ước
so_nguyen_to_1 = lambda n: n > 1 and sum(1 for i in range(1, n + 1) if n % i == 0) == 2

# Cách 2: Tổng các ước
so_nguyen_to_2 = lambda n: n > 1 and sum(i for i in range(1, n + 1) if n % i == 0) == n + 1

# Cách 3: Dùng any và căn bậc hai
so_nguyen_to_3 = lambda n: n > 1 and not any(n % i == 0 for i in range(2, int(math.sqrt(n)) + 1))

# Cách 4: Dùng filter + lambda
def F(k):
    return k > 1 and len(list(filter(lambda x: k % x == 0, range(1, k + 1)))) == 2

# ---------------- KẾT QUẢ ----------------

print("Cách 1:")
for i in range(1, 101):
    if so_nguyen_to_1(i):
        print(i, end=" ")

print("\n\nCách 2:")
for i in range(1, 101):
    if so_nguyen_to_2(i):
        print(i, end=" ")

print("\n\nCách 3:")
for i in range(1, 101):
    if so_nguyen_to_3(i):
        print(i, end=" ")

print("\n\nCách 4:")
for i in range(1, 101):
    if F(i):
        print(i, end=" ")