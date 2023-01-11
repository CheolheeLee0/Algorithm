# Author : Catveloper
# Problem : https://www.acmicpc.net/problem/10162
# 01/11 11:34

import sys
from collections import deque

def input():
  return sys.stdin.readline().rstrip()

T = int(input())

if T % 10 != 0:
    print(-1)
else:
    A = B = C = 0
    A = T // 300
    B = (T % 300) // 60
    C = (T % 300) % 60 // 10
    print(A, B, C)