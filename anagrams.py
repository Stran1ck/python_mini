def anagrams(word, words):
    words2 = []
    for i in words:
        if i not in words2:
            words2.append(i)
    for i in words2:
        if len(word) != len(i):
            words2.remove(i)
    words = []
    for i in words2:
        for j in i:
            if word.find(j) == -1 or word.count(j) != i.count(j):
                words.append(i)
                break
    for i in words:
        words2.remove(i)
    return words2




def anagrams1(word, words):
    return [item for item in words if sorted(item)==sorted(word)]



print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))
