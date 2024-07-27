a = 12
b = 18
x, y = a, b
while y:
    x, y = y, x % y
gcd = x
lcm = abs(a * b) // gcd
print(lcm)
