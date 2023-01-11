# Author : Catveloper
# Problem : https://www.acmicpc.net/problem/2217
# 01/11 11:23

import sys
from collections import deque

def input():
  return sys.stdin.readline().rstrip()

N = int(input())
lope_list = []
max_val = deque()

for i in range(N):
  lope_list.append(int(input()))

lope_list.sort(reverse=True)

for k in range(N):
  max_val.append(lope_list[k] * (k+1))

print(max(max_val))