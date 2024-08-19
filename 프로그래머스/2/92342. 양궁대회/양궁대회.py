from copy import deepcopy

max_gap = 0
max_list = []

# 최적의 결과 도출 후 점수 계산
def calc_score(apeach, lion):
    global max_gap, max_list
    apeach_score = 0
    lion_score = 0
    for i in range(11): # info의 길이만큼
        if apeach[i] == 0 and lion[i] == 0: # 어피치, 라이언 모두 못 맞힘
            continue
        if apeach[i] >= lion[i]: # 어피치가 맞힌 횟수가 라이언 횟수보다 크거나 같으면
            apeach_score += 10-i # 어피치가 점수 획득. 어피치에 점수 더해줌
        elif apeach[i] < lion[i]: # 라이언이 맞힌 횟수가 더 많으면
            lion_score += 10-i # 라이언에 점수 더해줌
            
    if lion_score > apeach_score: # 라이언 점수가 더 클 때
        gap = lion_score - apeach_score # 라이언과 어피치 점수차 저장
        if gap > max_gap: # 점수차가 최대인 리스트로 갱신
            max_gap = gap
            max_list = deepcopy(lion)
        elif gap == max_gap: # 점수차 최대이면 낮은 점수 많이 쏘는 걸로
            for i in range(10, -1, -1): # 10 9 ... 0
                if lion[i] > max_list[i]:
                    max_list = deepcopy(lion)
                    break
                elif lion[i] < max_list[i]:
                    break

def dfs(idx, lion, shot, apeach): # idx: 현재 점수 인덱스, shot: 라이언의 남은 화살 개수
    if shot == 0: # 남은 화살 개수 없으면 점수 계산
        calc_score(apeach, lion)
        return
    if idx == 11: # 모든 인덱스 탐색했으면 종료
        return

    a_score = apeach[idx] # 어피치가 맞힌 화살 개수
    # 어피치가 맞힌 수보다 1개 많은 경우 라이언이 화살 쏠 수 있음
    # 라이언이 0발부터 어피치+1 까지의 경우의 수 모두 탐색
    # 각 점수에서 몇 발의 화살을 쏘는게 유리할지 모두 시도
    for num in range(a_score+2): # 어피치 2를 쏘면 라이언은 0~3
        if shot >= num: # 남은 화살이 쏠 수 있는 화살 수보다 많을 때만 진행
            lion[idx] = num # 라이언이 쏜 화살
            dfs(idx+1, lion, shot-num, apeach) # 다음 점수로 이동. 0일 때 모든 경우, 1일 때 모든 경우 ...
            lion[idx] = 0 # 재귀호출 끝나면 0으로 초기화하여 다른 경우의 수 탐색할 수 있도록

def solution(n, info):
    global max_list
    temp = [0 for _ in range(11)] # 라이언 리스트 0으로 초기화
    dfs(0, temp, n, info)

    if max_list:
        return max_list
    else:
        return [-1]