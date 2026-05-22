# k) Số lộc phát

# Cách 1: dùng all
so_loc_phat_1 = lambda n: all(ch in "68" for ch in str(n))

# Cách 2: đếm số 6 và 8
so_loc_phat_2 = lambda n: (str(n).count("6") + str(n).count("8")) == len(str(n))

# l) Số lộc phát Palindrome
so_loc_phat_palindrome = lambda n: (
    str(n) == str(n)[::-1]
    and all(ch in "68" for ch in str(n))
)

# ---------------- KẾT QUẢ ----------------

print("k) Số lộc phát (Cách 1) từ 1 đến 1000:")
for i in range(1, 1001):
    if so_loc_phat_1(i):
        print(i, end=" ")

print("\n\nk) Số lộc phát (Cách 2) từ 1 đến 1000:")
for i in range(1, 1001):
    if so_loc_phat_2(i):
        print(i, end=" ")

print("\n\nl) Số lộc phát Palindrome từ 1 đến 10000:")
for i in range(1, 10001):
    if so_loc_phat_palindrome(i):
        print(i, end=" ")