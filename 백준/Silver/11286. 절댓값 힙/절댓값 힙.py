import heapq

n = int(input())
heap = []
for _ in range(n):
    num = int(input())
    if num != 0:
        heapq.heappush(heap, (abs(num), num)) # 절댓값 기준으로 heappush
    else:
        if heap: # heap이 비어있지 않으면
            print(heapq.heappop(heap)[1]) # 실제값을 pop
        else:
            print(0)