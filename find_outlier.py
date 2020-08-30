def find_outlier(integers):
    a = []
    b = []
    for i in integers:
        if i % 2 == 0:
            a.append(i)
        else:
            b.append(i)
    if len(a) == 1:
        return a[0]
    else:
        return b[0]


print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))
