# Author : Catveloper
# Problem : https://www.acmicpc.net/problem/10866
# 01/06 15:03
import sys
from collections import deque

def input():
  return sys.stdin.readline().rstrip()

N = int(input())
arr = input()
oper = '+-*/'
dic = {}
stack = []
d = deque()

for i in range(N):
  d.append(int(input()))

for i in arr:
  if i not in dic and i not in oper:
    dic[i] = d.popleft()

for i in arr:
  if i not in oper:
    stack.append(dic[i])
  else:
    if i == '+':
      a = stack.pop()
      b = stack.pop()
      stack.append(b+a)
    elif i == '-':
      a = stack.pop()
      b = stack.pop()
      stack.append(b-a)
    elif i == '*':
      a = stack.pop()
      b = stack.pop()
      stack.append(b*a)
    elif i == '/':
      a = stack.pop()
      b = stack.pop()
      stack.append(b/a)

print(f"{stack[0]:.2f}")
