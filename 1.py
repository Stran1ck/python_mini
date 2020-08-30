n = int(input())
c = 0
matrix = []
for i in range(n):
    a = [int(x) for x in input().split()]
    matrix.append(a)
for i in range(n):
    c += matrix[i][i]
print(c)
