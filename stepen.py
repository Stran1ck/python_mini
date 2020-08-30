n = int(input())
while n < 1000000000:
    n = int(str(n)[0]) * n
    if int(str(n)[0]) == 1:
        break
print(n)
