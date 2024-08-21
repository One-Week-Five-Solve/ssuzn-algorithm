N, K = map(int, input().split())
val = []
for i in range(N):
  num = int(input())
  val.append(num)
  
cnt = 0
val.sort(reverse = True)

for j in val:
  if K >= j:
    cnt += K // j
    K %= j
  
print(cnt)