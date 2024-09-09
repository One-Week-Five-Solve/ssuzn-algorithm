# 1사분면: x, y
# 2사분면: x, y + n//2
# 3사분면: x + n//2, y
# 4사분면: x + n//2, y + n//2
# 시작점의 색상과 다르면 4분할 반복
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
cnt0 = 0
cnt1 = 0
def sol(x, y, n):
    global cnt0, cnt1
    color = arr[x][y]
    # 주어진 영역 모두 같은 색인지 확인
    for i in range(x, x+n):
        for j in range(y, y+n):
            # 색상 하나라도 다르면 4분할 후 재귀 호출
            if arr[i][j] != color:
                sol(x, y, n//2)
                sol(x, y + n//2, n//2)
                sol(x + n//2, y, n//2)
                sol(x + n//2, y + n//2, n//2)
                return # 분할 후 더이상 처리 X
    
    # 색상 같으면 해당 색상 카운트 증가
    if color == 0:
        cnt0 += 1
    else:
        cnt1 += 1

sol(0, 0, n)
print(cnt0)
print(cnt1)