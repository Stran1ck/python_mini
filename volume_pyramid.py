a = float(input())
h = float(input())
if a <= 0 or h <= 0:
    print('error')
else:
    v = (a**2 * h) / (4 * 3**0.5)
    s = a**2 * 3**0.5 / 4 + (3 * a / 2) * (h**2 + a**2 / 12)**0.5
    print(round(v, 3), round(s, 3))
