# Author : Catveloper
# Problem : https://www.acmicpc.net/problem/1789
# 01/11 11:58

import sys
from collections import deque
import math

def input():
  return sys.stdin.readline().rstrip()

K = int(input())
n = 1

while n * (n+1) / 2 <= K:
  n += 1

print(n - 1)