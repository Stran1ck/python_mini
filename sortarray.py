def sort_array(source_array):
    a_key = []
    a_value = []
    a = []
    for key, value in enumerate(source_array):
        if value % 2 == 0:
            a.append(value)
        elif value % 2:
            a_key.append(key)
            a_value.append(value)
    a_value.sort()
    for i in range(len(a_value)):
        a.insert(a_key[i], a_value[i])
    return a


print(sort_array([5, 3, 2, 8, 1, 4, 7]))
print(sort_array([5, 3, 1, 8, 0, 7]))
print(sort_array([]))


# def sort_array(arr):
#   odds = sorted((x for x in arr if x%2 != 0), reverse=True)
#   return [x if x%2==0 else odds.pop() for x in arr]