# 9개로 분할 => 1/3로 나눔
# x, 
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
cnta = 0 # -1
cntb = 0 # 0
cntc = 0 # 1

def sol(x, y, n):
    global cnta, cntb, cntc
    color = arr[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if arr[i][j] != color:
                div = n//3 # 1/3로 나누기 위함
                sol(x, y, div)
                sol(x, y+div, div)
                sol(x, y+div*2, div)
                sol(x+div, y, div)
                sol(x+div, y+div, div)
                sol(x+div, y+div*2, div)
                sol(x+div*2, y, div)
                sol(x+div*2, y+div, div)
                sol(x+div*2, y+div*2, div)
                return
    if color == -1:
        cnta += 1
    elif color == 0:
        cntb += 1
    else:
        cntc += 1

sol(0, 0, n)
print(cnta, cntb, cntc, sep='\n')