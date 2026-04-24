def luy_thua(a, b):
    if b == 0:
        return 1
    return a * luy_thua(a, b - 1)

# Test
a, b = 2, 3
print("Lũy thừa:", luy_thua(a, b))