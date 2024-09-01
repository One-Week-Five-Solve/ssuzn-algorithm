n = int(input())
p = int(input())
graph = [[] for _ in range(n+1)] # 1번 인덱스 = 1번노드 맞추기 위해 n+1
for _ in range(p):
    x, y = map(int, input().split())
    # 양방향으로 연결될 수 있도록
    graph[x].append(y)
    graph[y].append(x)

def dfs(x, cnt):
    visited[x] = True
    for y in graph[x]:
        if not visited[y]:
            cnt = dfs(y, cnt+1)
    return cnt

visited = [False for _ in range(n+1)]
print(dfs(1, 0))