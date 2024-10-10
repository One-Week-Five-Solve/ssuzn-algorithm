# 3으로 나누기
# dp[9] = 3으로 나누기 또는 1 빼기
# 2로 나누기
# 1 빼기
# 위 세가지 연산을 최소로 사용하여 1을 만들기

n = int(input())
cnt = 0
dp = [0] * 1000001 # i를 만드는데 필요한 연산 횟수 저장

for i in range(2, n+1):
    dp[i] = dp[i-1] + 1 # 1로 빼는 경우

    if i % 3 == 0:
        dp[i] = min(dp[i//3] + 1, dp[i])
    
    if i % 2 == 0:
        dp[i] = min(dp[i//2] + 1, dp[i])

print(dp[n])