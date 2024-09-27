import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
arr.sort()
res = []
start, end = 0, n-1
val = sys.maxsize

while start < end:
    if abs(arr[start] + arr[end]) <= val:
        val = abs(arr[start] + arr[end])
        res = [arr[start], arr[end]]
    
    if arr[start] + arr[end] < 0:
        start += 1
    else:
        end -= 1

print(*res)