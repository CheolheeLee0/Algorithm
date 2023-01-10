# Author : Catveloper
# Problem : https://www.acmicpc.net/problem/1931
# 01/10 19:35

import sys
from collections import deque

def input():
  return sys.stdin.readline().rstrip()

n = int(input())

meetings = []

for _ in range(n):
    start, end = map(int, input().split(" "))
    meetings.append((start, end))
# 종료 시간을 오름차순 정렬하고, 시작 시간을 오름차순 정렬합니다
meetings.sort(key=lambda x: (x[1], x[0]))

time = 0
answer = 0
for s, e in meetings:
    if time <= s:
        time = e
        answer += 1

print(answer)