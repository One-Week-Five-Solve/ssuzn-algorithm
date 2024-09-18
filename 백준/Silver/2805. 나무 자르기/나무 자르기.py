n,m = map(int, input().split())
height = list(map(int, input().split()))
start = 0
end = max(height)

while start <= end:
    mid = (start + end) // 2
    sum = 0 # 자른 나무의 총합
    for i in range(n):
        if height[i] >= mid:
            sum += height[i] - mid

    # sum이 m과 같을 때도 수행 (가장 높은 m 찾기 위해)
    if sum >= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)