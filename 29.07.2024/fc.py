number = 36
factors = []
for i in range(1, number + 1):
    if number % i == 0:
        factors.append(i)
print(f"Factors of {number}: {factors}")
