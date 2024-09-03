n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input())))
cnt = 0
res = []

# 상하좌우
dx = [0, 0, 1, -1] 
dy = [1, -1, 0, 0]

def dfs(x, y):
    global cnt # 재귀적으로 호출되는 모든 dfs에서 동일한 cnt 변수 공유 & 각 호출에서 cnt 값이 유지, 업데이트
    
    if arr[x][y] == 1:
        cnt += 1
        arr[x][y] = 0 # 방문처리
        for i in range(4): # 상하좌우
            a = x + dx[i]
            b = y + dy[i]
            if 0 <= a < n and 0 <= b < n:  # 배열의 범위를 벗어나지 않도록 체크
                dfs(a, b) # 재귀적으로 인접한 노드 방문


for i in range(n):
    for j in range(n):
        if arr[i][j] == 1: # arr에서 1인 값만 dfs 처리
            dfs(i, j)
            res.append(cnt) # 방문한 카운트 저장
            cnt = 0 # 다음 단지를 위해 초기화

res.sort()
print(len(res))
for i in res:
    print(i)