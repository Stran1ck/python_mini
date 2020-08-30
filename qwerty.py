n = input()
m = input()
if len(n) < 7 and len(m) < 7:
    print('Short')
elif n == m:
    print('OK')
else:
    print('Difference')