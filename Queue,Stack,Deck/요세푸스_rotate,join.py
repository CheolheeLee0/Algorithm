# Author : Catveloper
# Problem : https://www.acmicpc.net/problem/1158
# 01/04 18:10

import sys
from collections import deque

def input():
  return sys.stdin.readline().rstrip()

N, K = map(int, input().split())
l = []
q = deque([i + 1 for i in range(N)])

while len(q) != 0:
  q.rotate(-K)
  l.append(q.pop())

print('<' + ', '.join(map(str, l)) + '>')