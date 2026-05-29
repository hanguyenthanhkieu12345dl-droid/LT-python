import math

# Lambda kiểm tra số chính phương
kiem_tra_chinh_phuong = lambda n: int(math.sqrt(n))**2 == n

# Lambda kiểm tra số hoàn thiện
kiem_tra_hoan_thien = lambda n: sum([i for i in range(1, n) if n % i == 0]) == n

# In số chính phương
print("Danh sách số chính phương từ 1 đến 10000:")

for i in range(1, 10001):
    if kiem_tra_chinh_phuong(i):
        print(i, end=" ")

print("\n")

# In số hoàn thiện
print("Danh sách số hoàn thiện từ 1 đến 10000:")

for i in range(1, 10001):
    if kiem_tra_hoan_thien(i):
        print(i, end=" ")