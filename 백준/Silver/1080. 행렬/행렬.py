# 1 1 1 0 0    
# 0 0 1 0 0
# 0 0 0 1 0
# 1 1 1 1 0 
# 3x3 부분행렬에서 한번만 뒤집히는 부분은 행렬의 왼쪽 맨 위
# 여기에 집중해서 맨 왼쪽 맨 위가 B와 같지 않으면 뒤집기
# 다 돌렸는데도 같지 않으면 -1 출력

n, m = map(int, input().split())
lstA = []
lstB = []
for _ in range(n):
    lstA.append(list(map(int, list(input().strip()))))
for _ in range(n):
    lstB.append(list(map(int, list(input().strip()))))

def flip(x, y):
    for a in range(x, x+3):
        for b in range(y, y+3):
            lstA[a][b] = 1 - lstA[a][b]

cnt = 0
for i in range(n-2):
    for j in range(m-2):
        if lstA[i][j] != lstB[i][j]:
            flip(i, j)
            cnt += 1

print(cnt if lstA == lstB else -1)