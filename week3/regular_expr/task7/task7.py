import re
import sys

pattern = r'\b[a]+\b'

test_lines = ["There’ll be no more Aaaaaaaaaaaaaaa",
              'AaAaAaA AaAaAaA']

for line in sys.stdin:
    line = line.rstrip()
    line = re.sub(pattern, "argh", line, count=1, flags=re.IGNORECASE)
    print(line)