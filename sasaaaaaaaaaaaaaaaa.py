a = set(map(int, input().split()))
b = set(map(int, input().split()))
c = list(a.symmetric_difference(b))
c.sort()
print(*c)
