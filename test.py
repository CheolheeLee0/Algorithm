import sys

from collections import deque
deq = deque()
deq = deque([1, 2, 3,4, 5, 7])
deq.appendleft(2)
deq.append(0)
deq.popleft()
deq.pop()
deq.extend([8, 9, 10])
deq.extendleft([0, 1, 2])
deq.remove(10)
deq.rotate(2)
print(deq)