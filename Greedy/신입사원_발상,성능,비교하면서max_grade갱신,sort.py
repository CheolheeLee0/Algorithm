# Author : Catveloper
# Problem : https://www.acmicpc.net/problem/1946
# 01/11 13:18

import sys
from collections import deque

def input():
  return sys.stdin.readline().rstrip()

T = int(input())

for _ in range(T):
  N = int(input())
  grade_list = []
  for i in range(N):
    grade1, grade2 = map(int, input().split())
    grade_list.append((grade1, grade2))
  grade_list.sort(key=lambda x:x[0])

  hire = 1
  max_grade2 = grade_list[0][1]

  for i in range(N):
    if grade_list[i][1] < max_grade2:
      hire += 1
      max_grade2 = grade_list[i][1]
  
  print(hire)

  # remove_set = set()
  # for i in range(len(grade_list)-1):
  #   for j in range(i+1, len(grade_list)):
  #     if grade_list[i][1] < grade_list[j][1]:
  #       remove_set.add(grade_list[j])
  
  # for e in remove_set:
  #   grade_list.remove(e)
  
  # print(len(grade_list))