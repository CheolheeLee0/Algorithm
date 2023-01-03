# Author : Catveloper
# Problem : https://www.acmicpc.net/problem/10828
# 01/02 15:00

import sys

def input():
  return sys.stdin.readline().rstrip()

N = int(input())

stack = []

for i in range(N):
  cmd = input().split()
  X = 0
  if len(cmd) == 2:
    X = cmd[1]
  cmd = cmd[0]

  if cmd == "push":
    stack.append(X)
  elif cmd == "pop":
    if len(stack) == 0:
      print(-1)
    else:
      print(stack[-1])
      stack.pop(-1)
  elif cmd == "size":
    print(len(stack))
  elif cmd == "empty":
    print(0 if len(stack) else 1)
  elif cmd == "top":
    if len(stack) == 0:
      print(-1)
    else:
      print(stack[-1])


