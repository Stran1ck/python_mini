s, t = input(), input()
i = 0
while t in s:
    a = s.find(t)
    i += 1
    s = s[a+1:]
print(i)