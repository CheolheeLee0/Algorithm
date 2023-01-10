# Author : Catveloper
# Problem : https://www.acmicpc.net/problem/2839
# 01/10 19:35

import sys
from collections import deque

def input():
  return sys.stdin.readline().rstrip()

N = int(input())

bag = 0
while N >= 0 :
    # 최선의 상황 5의 배수인 경우
    if N % 5 == 0:
        bag += (N // 5)
        print(bag)
        break
    # 최선의 상황인 5의 배수가 될 때까지 -3
    N -= 3  
    bag += 1
else :
    print(-1)
