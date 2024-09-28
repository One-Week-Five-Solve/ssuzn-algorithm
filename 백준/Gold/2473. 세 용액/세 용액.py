import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
arr.sort()
minvalue = sys.maxsize
res = []

for i in range(n-2):
    start = i+1
    end = n-1
    while start < end:
        tmp = arr[i] + arr[start] + arr[end]
        if abs(tmp) < minvalue:
            minvalue = abs(tmp)
            res = [arr[i], arr[start], arr[end]]
        
        if tmp < 0:
            start += 1
        else:
            end -= 1

print(*res)