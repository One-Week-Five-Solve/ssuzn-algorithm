n = int(input())
a = list(map(int, input().split()))

dp = [1 for _ in range(n)] # 수열 길이 저장 (가장 최소 길이 1)

for i in range(n): # 현재 값
    for j in range(i): # 이전 값
        if a[i] > a[j]: # 현재 값이 이전 값보다 크면 증가하는 수열 가능성
            dp[i] = max(dp[i], dp[j]+1) # 더 긴 길이의 수열 저장

print(max(dp))