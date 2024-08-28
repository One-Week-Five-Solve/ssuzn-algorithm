def solution(triangle):
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0: # 제일 왼쪽 값은 이전 줄의 제일 왼쪽값 + 현재 값 고정
                triangle[i][j] = triangle[i-1][j] + triangle[i][j]
            elif j == len(triangle[i]) - 1: # 제일 오른쪽 값도 동일
                triangle[i][j] = triangle[i-1][j-1] + triangle[i][j]
            else:
                triangle[i][j] = max(triangle[i-1][j], triangle[i-1][j-1]) + triangle[i][j]

    return(max(triangle[-1]))