n, k = map(int, input().split())


def hren(n1, k1):
    if k1 == 0:
        return 1
    else:
        if k1 > n1:
            return 0
        else:
            return hren(n1 - 1, k1) + hren(n1 - 1, k1 - 1)


print(hren(n, k))
