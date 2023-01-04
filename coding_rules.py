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
array = [[0]*m for _in range(n)]


# 5. tuple
# - indexing, slicing 가능, 특정 index 값 변경 불가
# - 조작 불가
# - 연결 : +
# - in
t = ()
t = (1, 2, 3)
t2 = (4, 5, 6)
t3 = t + t2

print(4 in t3)

# 6. dict
# - {key: value} 형태 : {'name': 'chlee', 'no': 2018}
# - O(1) 성능 : key값으로 value 조회
d = {}
d = {'name': 'chlee', 'no': 2018}


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