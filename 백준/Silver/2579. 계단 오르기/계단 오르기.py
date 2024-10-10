# 연속한 세 계단 불가
# 다음 계단 또는 다다음 계단 가능
# 마지막 계단 반드시 밟아야 함 (arr[i] 필수)


n = int(input())
arr = []
dp = [0] * n # 중간 결과값 저장

for _ in range(n):
    a = int(input())
    arr.append(a)

if n == 1: # 계단 하나일 때
    print(arr[0])
elif n == 2: # 계단 두개일 때
    print(arr[0] + arr[1]) # 첫번째 두번째 계단
else:
    dp[0] = arr[0] 
    dp[1] = arr[0]+arr[1] 
    dp[2] = max(arr[0] + arr[2], arr[1] + arr[2]) 

    for i in range(3, n):
        dp[i] = max(arr[i] + arr[i-1] + dp[i-3], arr[i] + dp[i-2])
    
    print(dp[n-1])