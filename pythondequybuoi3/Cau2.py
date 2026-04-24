def giai_thua(n):
    if n == 0 or n == 1:
        return 1
    return n * giai_thua(n - 1)

# Test
n = 5
print("Giai thừa:", giai_thua(n))