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

# 3. str : indexing, slicing 가능, 특정 index 값은 변경 불가능
s = "hello world"
print(s)
print(s[1:5])
print(s[1])
# s[1] = 'q' # immutable, 변경 불가능
# print(s)

