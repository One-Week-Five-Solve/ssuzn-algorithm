N = int(input())
num = list(map(int, input().split()))
num.sort()
res = 0
for i in range(1, N+1):
  res += sum(num[0:i])

print(res)
  