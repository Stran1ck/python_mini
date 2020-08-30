def generate_hashtag(s):
    if s:
        s = s.title()
        s = s.split()
        s.insert(0, '#')
        if len(s) <= 1:
            return False
        s = ''.join(str(x) for x in s)
        if len(s) > 140:
            return False
        return s
    return False


print(generate_hashtag('Codewars'))


def generate_hashtag(s):
    output = "#"

    for word in s.split():
        output += word.capitalize()

    return False if (len(s) == 0 or len(output) > 140) else output



def generate_hashtag(s):
    ans = '#'+ str(s.title().replace(' ',''))
    return s and not len(ans)>140 and ans or False