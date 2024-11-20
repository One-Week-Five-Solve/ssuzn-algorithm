t = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = [(x, y)]
    visited[x][y] = 0
    
    while q:
        x, y = q.pop(0)
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
                
            if visited[nx][ny] == 1:
                q.append((nx, ny))
                visited[nx][ny] = 0
        

for i in range(t):
    m, n, k = map(int,input().split())
    visited = [[0]*(n) for _ in range(m)]
    cnt = 0

    for j in range(k):
        x, y = map(int, input().split())
        visited[x][y] = 1

    for a in range(m):
        for b in range(n):
            if visited[a][b] == 1:
                bfs(a,b)
                cnt += 1

    print(cnt)
             