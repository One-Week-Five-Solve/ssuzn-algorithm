import sys

input = sys.stdin.readline

n, m = map(int, input().split())
poketmon = dict()
num = dict()

for i in range(1, n+1):
    x = input().strip() # 줄바꿈 문자 제거
    poketmon[x] = i # {포켓몬 이름 : 번호}
    num[i] = x # {번호 : 포켓몬 이름}

for _ in range(m):
    y = input().strip()
    if y.isdigit(): # 입력이 숫자값이면
        print(num[int(y)])
    else:
        print(poketmon[y])