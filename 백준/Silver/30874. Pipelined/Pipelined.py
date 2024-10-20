# 가장 많은 단계를 거쳐야 하는 작업 maxSi
# 마지막 작업이 끝나는 시점에서 최소 maxSi의 시간이 필요
# 마지막 작업 배치하기까지 필요한 시간은 나머지 n-1개의 작업 처리하는 시간
# 1초의 간격이 들어가야 하기 때문

# 첫번째 작업 5: 0 -> 5
# 두번째 작업 7: 1 -> 8
# 세번쩨 작업 8: 2 -> 10
# 네번째 작업 11: 3 -> 14

import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
arr.sort()
maxSi = arr[-1] # 가장 오래 걸리는 작업
minTime = (n-1) + maxSi # 앞의 3개 작업 처리하는데 3초 간격 소요
print(minTime)
