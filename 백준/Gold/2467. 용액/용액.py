import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))

start = 0
end = n-1
val = sys.maxsize
res = []

while start < end:
    # 절댓값이 더 작은 수 저장
    if abs(arr[start] + arr[end]) <= val:
        res = [arr[start], arr[end]]
        val = abs(arr[start] + arr[end])
        
    if arr[start] + arr[end] < 0: # 음수 값이 더 크면
        start += 1
    else: # 양수 값이 더 크면
        end -= 1

print(*res)