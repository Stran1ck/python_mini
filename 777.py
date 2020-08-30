a = input().lower()
x = 0
for i in a:
    if a.count(i) > x:
        x = a.count(i)
print(x)
