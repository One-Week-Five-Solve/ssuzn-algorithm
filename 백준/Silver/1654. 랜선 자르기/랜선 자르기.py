import sys

k, n = map(int, sys.stdin.readline().split())
len = [int(sys.stdin.readline()) for _ in range(k)]
start = 1 
end = max(len)

while start <= end:
    mid = (start + end) // 2
    sum = 0
    for i in len:
        sum += i // mid

    if sum < n:
        end = mid - 1
    else:
        start = mid + 1
        
print(end)