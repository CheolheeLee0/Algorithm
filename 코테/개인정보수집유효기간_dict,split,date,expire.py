# Author : Catveloper
# Problem : https://school.programmers.co.kr/learn/courses/30/lessons/150370
# 01/10 18:40~19:14

def solution(today, terms, privacies):
    answer = []
    # ['2022', '05', '19']
    t = list(map(int, today.split('.'))) # 현재 날짜
    # {'A: 6', 'B':12, 'C': 3}, 만료 기한
    td = {}
    for i in range(len(terms)):
        a, m = terms[i].split() 
        td[a] = int(m)
    
    ld = {}
    for j in range(len(privacies)):
        dt_str, a = privacies[j].split()
        # ['2022', '05', '19']
        dt = list(map(int, dt_str.split('.')))
        if check_expire(t, td, dt, a):
            answer.append(j+1)
    
    return answer
# 현재 날짜 t
# 만료 기한 td
# 수집 일자 dt
# 수집 방침 a
def check_expire(t, td, dt, a):
    print(t, td, dt, a)
    t_y, t_m, t_d = t[0], t[1], t[2]
    l_y, l_m, l_d = dt[0], dt[1], dt[2]
    
    # k : A,B,C
    # v : [2021,5,2], 
    # td[k] : 만료기한
    diff = 12 * (t_y - l_y) + (t_m - l_m) + (t_d - l_d)/30
    if diff >= td[a]:
        return True
    return False
    
answer = solution("2022.05.19",	["A 6", "B 12", "C 3"],	["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"])

print(answer)