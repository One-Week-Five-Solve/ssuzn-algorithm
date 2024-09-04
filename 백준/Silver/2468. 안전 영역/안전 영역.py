# max_height까지 물에 잠기지 않는 안전한 영역의 개수 저장 -> 그 중 가장 큰 값
import sys
sys.setrecursionlimit(100000) # 재귀 한도 늘려줌 (런타임에러 방지)

n = int(input())
arr = []
max_height = 0
res = 0

for i in range(n):
    a = list(map(int, input().split()))
    arr.append(a)
    
    for j in a:
        if j > max_height:
            max_height = j

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y, height):
    visited[x][y] = True
    for i in range(4): # 상하좌우
        a = x + dx[i]
        b = y + dy[i]
        if 0 <= a < n and 0 <= b < n and not visited[a][b] and arr[a][b] > height: # 비의 양보다 높아야 함
            dfs(a, b, height)

for i in range(max_height): # 0부터 최대 높이까지 비의 양 변화시키며 탐색
    cnt = 0 # 안전한 영역 개수 저장
    visited = [[False] * n for _ in range(n)]
    for j in range(n): 
        for k in range(n):
            if arr[j][k] > i and not visited[j][k]:
                dfs(j, k, i)
                cnt += 1
                visited[j][k] = True
    res = max(res, cnt)

print(res)
    