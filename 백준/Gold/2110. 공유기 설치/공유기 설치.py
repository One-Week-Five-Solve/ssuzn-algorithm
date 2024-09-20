n, c = map(int, input().split())
x = [int(input()) for _ in range(n)]
x.sort()
start = 1 # 최소 거리
end = x[-1] - x[0] # 최대 거리
res = 0 # 설치한 공유기 수

while start <= end:
    mid = (start + end) // 2
    install = 1 # 설치할 공유기의 수
    cur = x[0] # 현재 설치할 공유기
    
    for i in range(n):
        if x[i] - cur >= mid: # 설정한 mid 거리보다 크면 공유기 설치
            install += 1
            cur = x[i]
    
    # 설치한 공유기 수가 c보다 많거나 적으면 재탐색
    if install >= c:
        start = mid + 1
        res = mid
    else:
        end = mid - 1

print(res)