dict1 = {x: {} for x in range(11)}
print(dict1)
while input():
    key, value1, value2 = [i for i in input().split()]
    key = int(key)
    dict2 = dict(zip([value1], [value2]))
    if dict1.get(key):
        if value1 in dict1[key]:
            dict1[key][value1] = dict1[key][value1] + dict2[value1]
        else:
            dict1[key][value1] = dict2[value1]
print(dict1)
