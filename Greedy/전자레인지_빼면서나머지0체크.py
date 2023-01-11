# Author : Catveloper
# Problem : https://www.acmicpc.net/problem/10162
# 01/11 11:34

import sys
from collections import deque

def input():
  return sys.stdin.readline().rstrip()

A, B, C = 300, 60, 10
A_cnt, B_cnt, C_cnt = 0, 0, 0

T = int(input())

while T >= 0:
  if T % 300 == 0:
    A_cnt = T // 300
    T = 0
    break
  elif T < 300 and T % 60 == 0:
    B_cnt = T // 60
    T = 0
    break
  T -= 10
  C_cnt += 1

if T == 0:
  print(f'{A_cnt} {B_cnt} {C_cnt}')
else:
  print(-1)