import sys

# 1. 소수점 붙이면 실수형
a = 5.
b = .7
print(a) # 5.0
print(b) # 0.7
print(type(a)) # <class 'float'>
print(type(b)) # <class 'float'>


# 2. 실수는 round 함수로 비교하기
a = 0.3 + 0.6
if a == 0.9:
  print(True)
else:
  print(False)
 # 결과 : False

# round(수, 자리 수) 반올림
a = round(0.3 + 0.6, 1)  # 0.9


# 3. str
# - indexing, slicing 가능, 특정 index 값은 변경 불가능
s = "hello world"
print(s)
print(s[1:5])
print(s[1])
# s[1] = 'q' # immutable, 변경 불가능
# print(s)


# 4. list
# - indexing, slicing 가능, 특정 index 값 변경 가능
# - append(x), insert(i, x), extend(list), remove(x), pop(i)
# - sort(reverse=True)
# - enumerate(list)
# - all, any
l = []
l = [1, 2, 3]
l.append(4)
l.insert(2, 5)
l.extend([6,7,8])
l.remove(4)
l.pop(2)
l.sort(reverse=True)

a = [12, 19, 34, 21, 50]
for x in enumerate(a):
  print(x) # (0, 12)\n (1, 19)\n ... (4, 50)\n 튜플로 출력

for x in enumerate(a):
  print(x[0], x[1]) # 0 12\n 1 19\n ... 4 50\n 
  
for i, val in enumerate(a):
  print(i, val) # 0 12\n 1 19\n ... 4 50\n

a = [11, 12, 42, 38, 7]
# all(iterable 리스트, 튜플, 딕셔너리 등)
# 모든 요소가 참이면 True, 하나라도 거짓이면 False
a = [11, 12, 42, 38, 7]
if all(60 > x for x in a):
  print("모든 원소가 60 미만입니다.")

# all(iterable 리스트, 튜플, 딕셔너리 등)
# 요소가 하나라도 참이면 True, 전부 거짓이면 False
if any(10 > x for x in a):
  print("20미만인 원소가 존재합니다.")

# N*M 2차원 리스트 초기화 할 때 (세로 N & 가로 M)
n, m = 2, 3
array = [[0]*m for _ in range(n)]


# 5. tuple
# - indexing, slicing 가능, 특정 index 값 변경 불가
# - 조작 불가
# - 연결 : +
# - in, count(x), index(x)
t = ()
t = (1, 2, 3)
t2 = (4, 5, 6)
t3 = t + t2

print(4 in t3)

# 6. dict
# - {key: value} 형태 : {'name': 'chlee', 'no': 2018}
# - O(1) 성능 : key값으로 value 조회
# - keys(), values()
d = {}
d = {'name': 'chlee', 'no': 2018}
print(d.keys())
print(d.values())
print(list(d.keys())

# 7. set
# - 중복 불가, 순서 없음
# - O(1) 성능 : 원소로 조회하므로
# - add(x), update(list), remove(x), discard(x)
s = set() # 주의 : {}로 초기화하면 dict가 생성됨
s = {1, 2, 3}
s.add(4)
s.update([6,7,8])
s.remove(2) # 없으면 KeyError 발생
s.discard(1) # 없어도 KeyError가 발생하지 않음

i = {1,2,3,4,5}
j = {3,5,7,9}
# - 합집합
print(i|j) # {1, 2, 3, 4, 5, 7, 9}
print(i.union(j)) # {1, 2, 3, 4, 5, 7, 9}
# - 교집합
print(i&j) # {3, 5}
print(i.intersection(j)) # {3, 5}
# - 차집합
print(i-j) # {1, 2, 4}
print(i.difference(j)) # {1, 2, 4}
# - 대칭차집합
print(i^j) # {1, 2, 4, 7, 9}
print(i.symmetric_difference(j)) # {1, 2, 4, 7, 9}  


# 8. 문자열 내장함수
# - lower(), upper(), find(x), count(x)
# - 연결 : +
s = "HapPineSS"
s.lower()
s.upper()
s.find("H")
s.count("s")

a = "ABC" + "DEF"
b = "Hello"
c = "World"
print(a) # ABCDEF
print(b + " " + c) # Hello World


# 9. cheat sheet
import sys

# 9.1. 입력 함수
def input():
  return sys.stdin.readline().rstrip()

# 9.2. 여러 입력을 여러 변수로 받기
'''
[입력 예시]
1 2 3 4
'''
a, b, c, d = map(int, input().split())
print(a, b, c, d) # 1, 2, 3, 4


# 9.3. 여러 입력을 한 리스트 변수로 받기
'''
[입력 예시]
1 3 5 7 9 10
'''
a = list(map(int, input().split()))
print(a) # [1, 3, 5, 7, 9, 10]

'''
[입력 예시]
A B C D E
'''
a = list(input().split())
print(a) # ['A', 'B', 'C', 'D', 'E']


# 9.4. 리스트의 중복 제거, 정렬하기
a = [3, 1, 5, 8, 5, 10, 7, 1]
print(a)
b = list(set(a)) # [1, 3, 5, 7, 8, 10]
c = sorted(list(set(a))) # [1, 3, 5, 7, 8, 10]
d = sorted(list(set(a)), reverse=True) # [10, 8, 7, 5, 3, 1]


# 9.5. 리스트의 총 합계, 평균 구하기
# - sum(list), round(sum(list) / N, 0) 
# - for문 대신 sum 사용하면 편하다
N = int(input()) # 개수
a = list(map(int, input().split())) # 점수 리스트 입력
total = sum(a)
avg = int(round(total/N, 0)) # 평균을 첫째 자리에서 반올림


# 9.6. 리스트 반복문에서 리스트의 원소 여러 번 사용할 때 (enumerate)
score = [80, 83, 95, 87, 93, 71]
for i, val in enumerate(score):
  if val > 90: # "score[i] < 90" 대신 짧고 편하게 사용 가능
    print("B")
  elif val > 80:
    print("C")
  elif val > 70:
    print("D")


# 9.7. 리스트의 원소 세기 (dict)
s = [1, 3, 4, 2, 3, 4, 1, 3]
cnt = {} # dictionary 생성
for x in s:
  if x in cnt:
    cnt[x] += 1
  else:
    cnt[x] = 1


# 9.8. dict value로 key값 찾기 (items())
for key, value in cnt.items():
  if value == "찾을 value 값":
    print(key, end=' ') # value에 해당하는 key 값 출력


# 9.9. 리스트를 문자열로 변환하기 (join)
arr = ['H', 'a', 'P', 'p', 'Y']
print(type(''.join(arr))) # <class 'str'>
print(''.join(arr))
a = ['0', '1', '3', '6']
print(int(''.join(a))) # 136


# 9.10. 두 변수 값 바꾸기
a, b = b, a


# 9.11. 연속하는 값들을 합하여 M이 되는 경우의 수
# - lt_idx와 rt_idx를 (왼쪽 끝 idx, 오른쪽 끝 idx) 지정하고, 
# - 합이 M보다 크면 lt에 1을 더하고 작으면 rt에 1을 더하면서 한 칸씩 이동


# 9.12. 딕셔너리 ‘key’로 존재 여부 확인
d = {'사과':1, '배':2}
if '사과' in d:
  print("yes")


# 9.13. 딕셔너리를 key 또는 value 기준으로 정렬
a = {'Tom': 90, 'Liz': 75, 'John': 67, 'Mia': 92}

print(a.keys()) # dict_keys(['Tom', 'Liz', 'John', 'Mia'])
print(list(a.keys())) # ['Tom', 'Liz', 'John', 'Mia']
print(sorted(a.keys())) # ['John', 'Liz', 'Mia', 'Tom']
print(sorted(a.keys(), reverse=True)) # ['Tom', 'Mia', 'Liz', 'John']

# 튜플 자료형으로 리턴
print(sorted(a.items())) 
# 결과 : [('John', 67), ('Liz', 75), ('Mia', 92), ('Tom', 90)]
print(sorted(a.items(), reverse=True)) 
# 결과 : [('Tom', 90), ('Mia', 92), ('Liz', 75), ('John', 67)]

# 람다식 key값 기준 정렬
print(sorted(a.items(), key=lambda x: x[0])) 
# 결과 : [('John', 67), ('Liz', 75), ('Mia', 92), ('Tom', 90)]
print(sorted(a.items(), key=lambda x: x[0], reverse=True)) 
# 결과 : [('Tom', 90), ('Mia', 92), ('Liz', 75), ('John', 67)]

# 람다식 value값 기준 정렬
print(sorted(a.items(), key=lambda x: x[1]))
# 결과 : [('John', 67), ('Liz', 75), ('Tom', 90), ('Mia', 92)]
print(sorted(a.items(), key=lambda x: x[1], reverse=True))
# 결과 : [('Mia', 92), ('Tom', 90), ('Liz', 75), ('John', 67)]


# 9.14. 2차원 리스트 입력 받기
'''
[입력 예시]
5
0 2 1 1 0
1 1 1 1 2
0 2 1 2 1
0 2 1 1 0
0 1 1 1 2
'''
n = int(input())
arr = list(list(map(int, input().split())) for _ in range(n))


# 9.15. 이분 탐색
a.sort() # 먼저 정렬
lt = 0 # 시작 값
rt = n-1 # 끝 값

while lt <= rt:
  mid = (lt + rt) // 2
  if a[mid] < m:
    lt = mid + 1
  elif m < a[mid]:
    rt = mid - 1
  elif m == a[mid]:
    print(mid+1)
    break


# 9.16. min, max
max_val = max(max_val, tmp)
min_val = min(min_val, tmp)


# 9.17. list 2개로 dictionary를 생성하기
key = ['Alex', 'Jess', 'Dilan', 'Mei', 'Teddy']
value = [80, 90, 95, 67, 88]
key_val = [key, value]
landmark_dict = dict(zip(*key_val))


# 9.18. list 비어있는지 확인
arr = []
if not arr:
  print("empty")
if arr:
  print("not empty")


# 9.19. 마지막 요소 가져오기, 제거하기
arr = [1, 3, 5, 2, 4]
print(arr[-1]) # 4
arr.pop()


# 9.20. deque
# - O(1)성능 : deque는 양 끝 엘리먼트의 append와 pop이 압도적으로 빠르다. 

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