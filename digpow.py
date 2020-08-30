def dig_pow(n, p):
    x = 0
    for i in range(len(str(n))):
        x += int(str(n)[i])**(p + i)
    if x % n == 0:
        return x // n
    return -1


print(dig_pow(89, 1))
