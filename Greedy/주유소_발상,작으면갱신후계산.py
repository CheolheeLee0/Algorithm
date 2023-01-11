# Author : Catveloper
# Problem : https://www.acmicpc.net/problem/13305
# 01/11 12:09

import sys
from collections import deque

def input():
  return sys.stdin.readline().rstrip()

N = int(input())
road = list(map(int, input().split()))
oil_price = list(map(int, input().split()))

res = 0
m = oil_price[0]

for i in range(N - 1):
  if oil_price[i] < m:
    m = oil_price[i]
  res += road[i] * m

print(res)