from collections import deque

n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # 미로 범위 벗어나지 않고, 이동할 수 있는 경로(1)인 경우에만
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 1:
                arr[nx][ny] = arr[x][y] + 1 # 이동한 위치에 최단 경로 길이 기록
                queue.append((nx, ny))
    return arr[n-1][m-1]

print(bfs(0, 0))