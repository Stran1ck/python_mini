def duplicate_encode(word):
    a = []
    b = []
    for i in word.lower():
        if i in a:
            b.append(i)
        else:
            a.append(i)
    a = ''
    for i in word.lower():
        if i in b:
            a += ')'
        else:
            a += '('
    word = a
    return word


duplicate_encode("Success")
