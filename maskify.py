def maskify(cc):
    if len(cc) > 4:
        cc = '#' * (len(cc) - 4) + cc[-4:len(cc) + 1]
    return cc

print(maskify("1"))