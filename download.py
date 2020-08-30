from urllib.request import urlopen
html = urlopen("https://stepik.org/media/attachments/lesson/209717/1.html").read().decode('utf-8')
s = str(html)
a = s.count('Python')
b = s.count('C++')
print(a, b)
if a > b :
    print('Python')
else:
    print('C++')