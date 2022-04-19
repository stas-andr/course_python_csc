import re
import sys

pattern = r'\b(\w+)\1\b'

lines_test = ['blabla is a tandem repetition',
              '123123 is good too',
              'go go',
              'aaa']

for line in sys.stdin:
    line = line.rstrip()
    search = re.search(pattern, line)
    if search:
        print(line)