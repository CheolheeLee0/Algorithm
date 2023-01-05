# Author : Catveloper
# Problem : https://www.acmicpc.net/problem/2164
# 01/05 16:05
import sys
from collections import deque

def input():
  return sys.stdin.readline().rstrip()

N = int(input())

d = deque([i+1 for i in range(N)])

for i in range(N-1):
  d.popleft()
  d.rotate(-1)

print(d[0])