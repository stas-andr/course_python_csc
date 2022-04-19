import re
import sys

pattern = "human"

test_lines = ['I need to understand the human mind',
              'humanity']

for line in sys.stdin:
    line = line.rstrip()
    line = re.sub(pattern, "computer", line)
    print(line)