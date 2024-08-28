def self_number_check(n):
    arr = list(range(1, n+1))
    res = []
    for i in range(1, n+1):
        num = i # 85
        for j in str(i): # 8 5
            num += int(j) # 85+8+5
        res.append(num)
    selfNum = list(set(arr) - set(res)) # 리스트끼리의 빼기 연산 안됨. set으로 변경하여 수행
    selfNum.sort()
    for i in selfNum:
        print(i)

self_number_check(10000)