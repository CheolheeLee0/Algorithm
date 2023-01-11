# Author : Catveloper
# Problem : https://www.acmicpc.net/problem/10610
# 01/11 12:33

import sys
from collections import deque

def input():
  return sys.stdin.readline().rstrip()


s = list(input())

if '0' not in s:
  print(-1)
else:
  num_list = list(map(int, s))
  if sum(num_list) % 3 != 0:
    print(-1)
  else:
    num_list.sort(reverse=True)
    print(''.join(map(str, num_list)))
