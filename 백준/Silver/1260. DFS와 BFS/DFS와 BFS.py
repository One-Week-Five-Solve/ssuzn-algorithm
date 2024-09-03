from collections import deque

def dfs(start):
    visited[start] = True
    print(start, end=' ')
    
    for i in arr[start]:
        if not visited[i]:
            dfs(i)

def bfs(start):
    queue = deque([start]) # 방문할 곳을 순서대로 넣을 큐
    visited[start] = True
    while queue: # 큐 안에 데이터 없을 때까지 실행
        v = queue.popleft()
        print(v, end=' ')
        for i in arr[v]: # 해당 원소와 연결된 방문하지 않은 원소들을 큐에 삽입
            if not visited[i]:
                visited[i] = True 
                queue.append(i)
    
    
n, m, v = map(int, input().split())
arr = [[] for _ in range(n+1)]

for  _ in range(m):
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)
    
for i in arr:
    i.sort() # 정점 번호가 작은 것부터 먼저 방문

visited = [False] * (n+1)
dfs(v)
print()
visited = [False] * (n+1)
bfs(v)