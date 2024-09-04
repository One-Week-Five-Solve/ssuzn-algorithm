from collections import deque
n, k = map(int, input().split())
visited = [0] * 100001 # 방문 위치에 방문 시간 저장

def bfs(start):
    queue = deque([start])
    
    while queue:
        v = queue.popleft() # 현재 위치
        if v == k: # 동생 위치에 도착하면, 방문시간 반환
            return visited[v]
        # 동생을 찾을 때까지 3가지 경우 체크
        for i in (v-1, v+1, 2*v):
            if 0 <= i <= 100000 and not visited[i]:
                visited[i] = visited[v] + 1 # 현재 위치 시간 + 1초
                queue.append(i) # 이동한 위치 큐에 추가

print(bfs(n))