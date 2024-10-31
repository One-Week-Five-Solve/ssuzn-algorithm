from collections import deque

n = int(input())
size = list(map(int, input().split()))
micro = deque([i + 1, size] for i, size in enumerate(size))

while len(micro) > 1: # 미생물 하나 남을 때까지
    next_days = deque() # 다음날 미생물
    
    while micro:
        now = micro.popleft()
        left, right = 0, 0
        
        if next_days:
            left = next_days.pop()
        if micro:
            right = micro.popleft()

        new = now[:]
        
        if left:
            if now[1] >= left[1]:
                new[1] += left[1]
            else:
                next_days.append(left)
        if right:
            if now[1] >= right[1]:
                new[1] += right[1]
            else:
                micro.appendleft(right)
        next_days.append(new)
    micro = deque(list(next_days)[:])

print(micro[0][1])
print(micro[0][0])