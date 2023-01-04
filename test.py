import sys


s = [1, 3, 4, 2, 3, 4, 1, 3]
cnt = {} # dictionary 생성
for x in s:
  if x in cnt:
    cnt[x] += 1
  else:
    cnt[x] = 1
  

print(cnt)