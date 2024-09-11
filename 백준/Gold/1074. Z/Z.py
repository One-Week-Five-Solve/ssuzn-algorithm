n, r, c = map(int, input().split())
res = 0 # 결과값 저장 변수. 각 사분면의 값을 차례로 더해줌
        
while n > 0: # n이 0이 될 때까지 반복
    std = 2 ** (n-1) # 각 사분면의 크기
    if r < std and c < std: # 2사분면
        res += std * std * 0
    elif r < std and c >= std: # 1사분면
        res += std * std * 1
        c -= std # 1사분면에서 다시 시작해야 하므로
    elif r >= std and c < std: # 3사분면
        res += std * std * 2
        r -= std # 3사분면에서 다시 시작해야 하므로
    else:
        res += std * std * 3
        r -= std 
        c -= std 
    n -= 1

print(res)