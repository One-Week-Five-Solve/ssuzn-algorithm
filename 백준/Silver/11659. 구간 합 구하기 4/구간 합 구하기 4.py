import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num = list(map(int, input().split()))
sm = 0 # 부분합
prt = [0] # 부분합 저장 배열
for i in num:
  sm = sm + i
  prt.append(sm)
  
for j in range(M):
  x, y = map(int, input().split())
  print(prt[y] - prt[x-1])
  