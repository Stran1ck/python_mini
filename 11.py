matrix_A = []
while True:
    i = [x for x in input().split()]
    if i[0] == "end":
        break
    matrix_A.append(i)
matrix_B = [[] for x in range(len(matrix_A))]
for j in range(len(matrix_A)):
    for i in range(len(matrix_A[j])):
        a = int(matrix_A[j - 1][i])
        b = int(matrix_A[j + 1 - len(matrix_A)][i])
        c = int(matrix_A[j][i - 1])
        d = int(matrix_A[j][i + 1 - len(matrix_A[j])])
        summa = a + b + c + d
        matrix_B[j].append(summa)
for x in range(len(matrix_B)):
    print(*matrix_B[x])
