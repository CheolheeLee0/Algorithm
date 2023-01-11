import sys
from collections import deque

d = deque()

d.append(1)
d.append(2)
d.append(3)

sorted(d, reverse=False)
print(d)