import re
import sys

pattern = r'\b(\w)(\w)(\w+)*'

test_lines = ['this is a text',
              "this' !is. ?n1ce"]

for line in sys.stdin:
    line = line.rstrip()
    line = re.sub(pattern, r'\2\1\3', line)
    print(line)

