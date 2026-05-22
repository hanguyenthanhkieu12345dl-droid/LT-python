import math

# i) Số Palindrome
so_palindrome = lambda n: str(n) == str(n)[::-1]

# j) Số nguyên tố Palindrome
so_nguyen_to_palindrome = lambda n: (
    n > 1 and
    str(n) == str(n)[::-1] and
    not any(n % i == 0 for i in range(2, int(math.sqrt(n)) + 1))
)

# ---------------- KẾT QUẢ ----------------

print("i) Các số Palindrome từ 0 đến 200:")
for i in range(0, 201):
    if so_palindrome(i):
        print(i, end=" ")

print("\n\nj) Các số nguyên tố Palindrome dưới 20000:")
for i in range(2, 20000):
    if so_nguyen_to_palindrome(i):
        print(i, end=" ")