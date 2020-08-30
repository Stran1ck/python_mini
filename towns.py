n = input().lower()
m = input().lower()
if n[-1] == m[0]:
    print('Good')
elif n[-1] == 'ь':
    if n[-2] == m[0]:
        print('Good')
else:
    print('Bad')