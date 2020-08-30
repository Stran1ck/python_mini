# matrix = [[] for j in range(5)]
# for i in range(len(matrix)):
#     matrix[i] = [int(j) for j in input().split()]
matrix = [[int(i) for i in input().split()] for j in range(5)]
a, b = 0, 0
for i in matrix:
    try:
        b = i.index(1)
    except ValueError:
        a += 1
        continue
    break
print(abs(2 - a) + abs(2 - b))
