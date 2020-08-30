d = int(input())
a = set()
b = set()
c = set()
for i in range(d):
    a.update({x for x in input().lower().split()})
d = int(input())
for i in range(d):
    b.update({x for x in input().lower().split()})
c = b - a
print(*c)
