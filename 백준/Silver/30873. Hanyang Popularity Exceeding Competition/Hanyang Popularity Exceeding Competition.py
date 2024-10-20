# |p-X| <= c -> 인기도 +1
n = int(input())
x = 0 # 현재 철민이의 인기도
popularity = [] # 유명인의 인기도 
meet = 0

for _ in range(n):
    p, c = map(int, input().split())
    if abs(p-x) <= c:
        meet += 1
        x += 1

print(x)