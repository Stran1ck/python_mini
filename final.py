import os
school = {}
students = {}
with open(os.path.join('/', 'home', 'andreas', 'Загрузки', 'dataset_3380_5 (4).txt'), 'r') as inf:
    for line in inf:
        s_0 = list(line.split())
        if school.get(int(s_0[0])):
            school[int(s_0[0])] += int(s_0[2])
            students[int(s_0[0])] += 1
        else:
            school[int(s_0[0])] = int(s_0[2])
            students[int(s_0[0])] = 1
    for key, value in school.items():
        school[key] = value / students[key]

with open('text2.txt', 'w') as ouf:
    for key in range(1, 12):
        line = str(key) + ' ' + str(school.get(key, '-'))
        ouf.write(line + '\n')
