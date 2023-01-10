# Author : Catveloper
# Problem : https://www.acmicpc.net/problem/2346
# 01/10 17:36

import sys
from collections import deque

def input():
  return sys.stdin.readline().rstrip()

N = int(input())
d = deque(list(map(int, input().split())))
id = deque(range(1, N+1))

while d:
  e = d[0]
  if e > 0:
    d.popleft()
    d.rotate(-e+1)
    print(id.popleft())
    id.rotate(-e+1)
  else:
    d.popleft()
    d.rotate(-e)
    print(id.popleft())
    id.rotate(-e)