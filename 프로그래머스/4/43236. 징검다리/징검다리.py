def solution(distance, rocks, n):
    answer = 0
    rocks.append(distance)
    rocks.sort()
    start = 1
    end = distance
    
    while start <= end:
        mid = (start + end) // 2 # 돌 사이 거리의 최솟값 중 최댓값 의미
        cnt = 0 # 제거한 돌
        prev = 0
        
        for i in range(len(rocks)):
            if rocks[i] - prev < mid:
                cnt += 1 # 돌 제거
            else: # mid보다 크면
                prev = rocks[i]
        
        if cnt > n:
            end = mid - 1
        else: # 거리의 최솟값을 구하는 문제
            start = mid + 1
            answer = mid
    
    return answer