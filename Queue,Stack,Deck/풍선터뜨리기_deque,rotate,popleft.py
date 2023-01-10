# Author : Catveloper
# Problem : https://www.acmicpc.net/problem/2346
# 01/10 17:36

# 1 ~ N 풍선 / 순환 리스트 / rotate / 
# 종이 (-N ~ N, 2N + 1) / 종이값만큼 이동 / + : 오른쪽, - : 왼쪽

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