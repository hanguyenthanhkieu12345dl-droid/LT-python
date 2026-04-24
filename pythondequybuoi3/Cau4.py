def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

# Test
a, b = 12, 18
print("UCLN:", gcd(a, b))