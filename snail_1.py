length_side_matrix = int(input())
length_array = length_side_matrix * length_side_matrix
matrix = [[0 for i in range(length_side_matrix)] for j in range(length_side_matrix)]
b = 1
c = 0
l1 = len(matrix) - 1
while length_array >= b:
    if length_array >= b:
        for i in range(c, length_side_matrix):
            matrix[c][i] = b
            b += 1
    if length_array >= b:
        for i in range(c + 1, length_side_matrix):
            matrix[i][length_side_matrix - 1] = b
            b += 1
    if length_array >= b:
        for i in range(l1 - 1, c - 1, -1):
            matrix[l1][i] = b
            b += 1
    if length_array >= b:
        for i in range(l1 - 1, c, -1):
            matrix[i][c] = b
            b += 1
        length_side_matrix -= 1
        c += 1
        l1 -= 1
for i in matrix:
    print(*i)
