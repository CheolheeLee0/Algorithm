# Author : Catveloper
# Problem : https://www.acmicpc.net/problem/1541
# 01/10 20:39

import sys
from collections import deque

def input():
  return sys.stdin.readline().rstrip()

s = input()
num_list = list(map(int, s.replace('+', '*').replace('-','*').split('*')))
op_list = deque()

for e in list(s):
  if e == '+' or e == '-':
    op_list.append(e)

num = num_list[0]
idx = 0
sum_val = num
find_minus = False
op_list_len = len(op_list)

while idx <= op_list_len - 1:
  op = op_list[idx]
  n = num_list[idx+1]
  if find_minus:
    sum_val -= n
  else:
    if op == '+':
      sum_val += n
    elif op == '-':
      sum_val -= n
      find_minus = True

  idx += 1
  
print(sum_val)