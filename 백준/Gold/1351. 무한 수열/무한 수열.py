# a[i] = a[i/p보다 크지 않은 정수] + a[i/q보다 크지 않은 정수]
# n이 너무 크기 때문에 리스트가 아닌 딕셔너리 사용
# dfs 이용하여 필요한 값만 가지고 오기 -> 시간초과 나지 않기 위해

import sys

input = sys.stdin.readline
n, p, q = map(int, input().split())

dict = {}
dict[0] = 1

def dfs(n):
    if n in dict:
        return dict[n]
    else:
        dict[n] = dfs(n//p) + dfs(n//q)
        return dict[n]
    
print(dfs(n))