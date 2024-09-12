n = int(input())
k = 0
len = 3 # moo
# n 길이의 moo 만드는데 필요한 k, len 구하기
while len < n:
    k += 1
    len = 2*len+(k+3)
def sol(n, k, len): 
    if n <= 3: # moo 인 경우 처리
        return ('m' if n == 1 else 'o')
    center = k+3
    prev = (len - center) // 2
    if n <= prev: # n이 왼쪽에 있을 때
        return sol(n, k-1, prev)
    elif n > prev+center: # n이 오른쪽에 있을 때
        return sol(n-(prev+center), k-1, prev)
    else: # n이 가운데 있을 때
        return ('m' if n == prev+1 else 'o')
    
print(sol(n, k, len))