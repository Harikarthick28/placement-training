n = 5  
triangle = [[1] * (i + 1) for i in range(n)]

for i in range(2, n):
    for j in range(1, i):
        triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

max_length = len(' '.join(map(str, triangle[-1])))
for row in triangle:
    print(' '.join(map(str, row)).center(max_length))
