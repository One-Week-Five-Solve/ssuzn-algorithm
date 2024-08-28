def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    
    i = 0 # people 첫번째 인덱스
    j = len(people) - 1 # people 마지막 인덱스
    while i <= j:
        if people[i] + people[j] <= limit:
            j -= 1
        i += 1
        answer += 1
    if len(people) == 1:
        answer += 1
            
    return answer