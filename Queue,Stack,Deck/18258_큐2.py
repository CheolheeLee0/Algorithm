import sys
from collections import deque

def input():
  return sys.stdin.readline().rstrip()


N = int(input())
queue = deque([])


for i in range(N):
  A = input().split()
  cmd = ''
  num = 0
  if len(A) == 2:
    num = A[1]
  cmd = A[0]

  if cmd == 'push':
    queue.append(num)
  elif cmd == 'pop':
    if len(queue) == 0:
      print(-1)
    else:
      print(queue.popleft())
  elif cmd == 'size':
    print(len(queue))
  elif cmd == 'empty':
    print(1 if len(queue) == 0 else 0)
  elif cmd == 'front':
    if len(queue) == 0:
      print(-1)
    else:
      print(queue[0])
  elif cmd == 'back':
    if len(queue) == 0:
      print(-1)
    else:
      print(queue[-1])

    