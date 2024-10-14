from collections import Counter
import sys

N = int(sys.stdin.readline())
arr = []
for i in range(N):
  num = int(input())
  arr.append(num)

# 산술평균  
print(round(sum(arr) / N))

# 중앙값
# / : 몫  // : 나누기 연산 후 소수점 이하의 수 버리고 정수만  % : 나머지
arr.sort()
median = arr[len(arr)//2]
print(median)
  
# 최빈값 Counter 사용
# Conter("apple") => {'p': 2, 'a': 1, 'l': 1, 'e': 1}
cnt = Counter(arr).most_common(2) 

if len(arr) > 1:
  if cnt[0][1] == cnt[1][1]:
    print(cnt[1][0])
  else:
    print(cnt[0][0])
else:
  print(cnt[0][0])
  
# 범위
print(max(arr) - min(arr))
