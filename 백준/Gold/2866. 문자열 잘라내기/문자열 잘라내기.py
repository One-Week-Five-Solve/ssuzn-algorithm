r, c = map(int, input().split())
arr = [list(input()) for _ in range(r)]
tmp = []

# 같은 열의 문자 tmp에 삽입
for C in range(c): # 열 순회
    s = ''
    for R in range(r):
        s += arr[R][C]
    tmp.append(s) # tmp = ['abz', 'lee', 'ftt']

for i in range(1, r): 
    check = set() # 중복 여부 확인 위한 집합. 각 열에서 i번째 행 이후의 문자를 잘라서 집합에 삽입
    # set은 중복 허용하지 않으므로 만약 특정 i에서 len(check)이 c와 다르면 중복된 문자 발생을 의미
    for s in tmp:
        check.add(s[i:])
    if len(check) != c:
        print(i-1) # 중복 발생 직전의 행 출력
        break # 중복 발생 시 종료
else:
    print(r-1) # 중복 없으면 r-1 출력 (모든 행 중복 없음)