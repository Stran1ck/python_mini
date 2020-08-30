s, a, b = input(), input(), input()
if a in b:
    print('Impossible')
else:
    i = 0
    while a in s:
        s = s.replace(a, b)
        i += 1
    print(i)
