a = [input() for i in range(int(input()))]
b = []
for i in a:
    if "соль" not in i:
        b.append(i)
print(*b, sep=', ')
