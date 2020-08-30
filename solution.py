def solution(s):
    v = [s[x:x + 2] for x in range(0, len(s), 2)]
    if len(s) % 2:
        v[-1] = s[-1] + '_'
    return v

print(solution('asdfads'))
