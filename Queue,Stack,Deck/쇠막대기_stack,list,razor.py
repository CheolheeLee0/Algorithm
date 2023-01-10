# Author : Catveloper
# Problem : https://www.acmicpc.net/problem/10799
# 01/10 18:07

import sys
from collections import deque

def input():
  return sys.stdin.readline().rstrip()


text = list(input().replace("()", "*"))
print(text)
stack = []
result = 0

for i in range(len(text)):
    if text[i] == "(":
        stack.append(0)
    elif text[i] == ")":
        stack.pop()
        result += 1
    else:  # 레이저 일때
        result += len(stack)
        print(result)

print(result)
