# Author : Catveloper
# Problem : https://www.acmicpc.net/problem/10866
# 01/10 17:35
import sys
from collections import deque

def input():
  return sys.stdin.readline().rstrip()

T = int(input())

for i in range(T):
    # 문서의 개수 N, 몇 번째인지 궁금한 문서의 위치 M
    N, M = map(int, input().split())
    # 문서 배열
    d = deque(list(map(int, input().split())))
    d_idx = deque(range(N))
    cnt = 1
    while True:
        if d[0] == max(d):
            if d_idx[0] == M:
              print(cnt)
              break
            else:
              d.popleft()
              d_idx.popleft()
              cnt += 1
        else:
            d.rotate(-1)
            d_idx.rotate(-1)