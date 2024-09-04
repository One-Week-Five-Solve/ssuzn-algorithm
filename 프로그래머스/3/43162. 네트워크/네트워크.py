def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    def dfs(node):
        visited[node] = True # 방문처리
    
        for i in range(n):
            if not visited[i] and computers[node][i] == 1: # 방문하지 않았고 연결되어 있을 때
                dfs(i)
    
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1
            
    return answer