a = input()
if len(a) % 2 == 0:
    a = list(a)
    d = []
    for i in range(len(a)):
        d.append(int(a[i]))
    b = d[:len(a)//2]
    c = d[len(a)//2:]
    if sum(b) == sum(c):
        print('YES')
    else:
        print('NO')
else:
    print('NO')
