import sys

import re

pattern = r'(cat){2,}'
for line in sys.stdin:
    line = line.rstrip()
    print(re.findall(pattern, line))
