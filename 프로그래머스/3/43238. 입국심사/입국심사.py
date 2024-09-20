def solution(n, times):
    answer = 0 # mid
    start = 1 # 최소 시간
    end = max(times) * n # 최대 시간
    
    while start <= end:
        mid = (start + end) // 2
        cnt = 0 # mid 시간동안 몇 명을 검사할 수 있는지 저장할 변수
    
        for i in times:
            cnt += mid // i
        
        if cnt >= n:
            answer = mid 
            end = mid - 1
        else:
            start = mid + 1
            
    return answer