# 뽑은 카드 중 카드 n/3장과 동전 coin개 가지고 시작
# 다음 라운드로 진행하기 위해 내야 할 카드 두장의 합은 n+1
# 뽑은 카드 중 동전 하나를 소모해서 가지거나 or 동전 소모하지 않고 버릴 수 있음

# 현재 지니고 있는 카드 중 합이 n+1을 만들 수 있는 두장의 카드가 있는지 확인
# 1. 만약 가능하면 두장을 내고 다음 라운드로 진출
# 2. 가능하지 않다면 코인 하나 사용하여 현재카드 & 뽑을카드에서 하나씩 골라 내기
# 3. 가능하지 않다면 코인 두개 사용하여 뽑을 카드에서 두장 내기
# 4. 현재카드 & 뽑을카드에도 없다면 스탑

from collections import deque

# 합이 n+1이 되는지 확인
def check(deck1, deck2, target):
    operand = set(deck2) # set 사용하여 검색 빠르게
    for card in deck1:
        if target - card in operand: # 현재카드 & 뽑을카드
            deck1.remove(card)
            deck2.remove(target - card)
            return True
    return False
        
def solution(coin, cards):
    answer = 1 # 게임 적어도 한번은 진행됨
    n = len(cards)
    current = cards[:n // 3] # 현재 카드
    deck = deque(cards[n // 3:]) # 뽑을 카드
    tmp = [] # 두장 뽑은 카드 저장
    
    while coin >= 0 and deck: # 코인이 0 이상이고 deck이 비어있지 않을 때까지
        # 카드 두장 뽑는다
        tmp.append(deck.popleft())
        tmp.append(deck.popleft())
        
        if check(current, current, n+1): # 현재 카드에서 만들 수 있을 때
            pass
        elif coin >= 1 and check(current, tmp, n+1): # 현재카드 & 뽑을 카드
            coin -= 1
        elif coin >= 2 and check(tmp, tmp, n+1): # 뽑을 카드에서 2장
            coin -= 2
        else: 
            break
        
        answer += 1
        
    return answer