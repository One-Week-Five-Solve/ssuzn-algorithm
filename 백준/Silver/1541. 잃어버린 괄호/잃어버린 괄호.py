num = input().split('-') # [3+4, 3, 10+24]
arr = [] # [7, 3, 34]

for i in num:
  sum = 0
  tmp = i.split('+') # 플러스 기준으로 나누기
  for j in tmp:
    sum += int(j) # 스플릿한 요소 더하기
  arr.append(sum) # 각 항의 덧셈 결과 저장
  
n = arr[0] 

for k in range(1, len(arr)):
  n -= arr[k]
  
print(n)
    