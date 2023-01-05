# Author : Catveloper
# Problem : https://www.acmicpc.net/problem/10866
# 01/05 16:25
import sys
from collections import deque

def input():
  return sys.stdin.readline().rstrip()

d = deque()

N = int(input())

for i in range(N):
  cmd_arr = input().split()
  x = int(cmd_arr[1]) if len(cmd_arr) == 2 else 0
  cmd = cmd_arr[0]

  if cmd == 'push_front':
    d.appendleft(x)
  elif cmd == 'push_back':
    d.append(x)
  elif cmd == 'pop_front':
    print(-1 if not d else d.popleft())
  elif cmd == 'pop_back':
    print(-1 if not d else d.pop())
  elif cmd == 'size':
    print(len(d))
  elif cmd == 'empty':
    print(0 if d else 1)
  elif cmd == 'front':
    print(d[0] if d else -1)
  elif cmd == 'back':
    print(d[-1] if d else -1)
