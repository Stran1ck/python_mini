def snail(snail_map):
    '''
    Snail Sort
    Given an n x n array, return the array elements arranged from outermost elements to the middle element,
    traveling clockwise.

    :param snail_map:
    array = [[1,2,3],
         [4,5,6],
         [7,8,9]]

    :return:
    snail(array) #=> [1,2,3,6,9,8,7,4,5]
    '''
    if snail_map == [[]]:
        return []
    len_side_matrix = len(snail_map)
    length_array = len_side_matrix * len_side_matrix
    counter = 1
    c = 0
    snail_map_2 = []
    l1 = len(snail_map) - 1
    while length_array >= counter:
        if length_array >= counter:
            for i in range(c, len_side_matrix):
                snail_map_2.append(snail_map[c][i])
                counter += 1
        if length_array >= counter:
            for i in range(c + 1, len_side_matrix):
                snail_map_2.append(snail_map[i][len_side_matrix - 1])
                counter += 1
        if length_array >= counter:
            for i in range(l1 - 1, c - 1, -1):
                snail_map_2.append(snail_map[l1][i])
                counter += 1
        if length_array >= counter:
            for i in range(l1 - 1, c, -1):
                snail_map_2.append(snail_map[i][c])
                counter += 1
            len_side_matrix -= 1
            c += 1
            l1 -= 1
    return snail_map_2


print(snail([[1, 2, 3], [8, 9, 4], [7, 6, 5]]))



# def snail(array):
#     a = []
#     while array:
#         a.extend(list(array.pop(0)))
#         array = zip(*array)
#         array.reverse()
#     return a




# def snail(array):
#     return list(array[0]) + snail(zip(*array[1:])[::-1]) if array else []