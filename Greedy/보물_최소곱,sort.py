# Author : Catveloper
# Problem : https://www.acmicpc.net/problem/1026
# 01/10 20:27

import sys
from collections import deque

def input():
  return sys.stdin.readline().rstrip()

N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)

S = 0

for i in range(N):
  S += A[i] * B[i]

print(S)