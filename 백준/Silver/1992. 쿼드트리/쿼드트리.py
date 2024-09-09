n = int(input())
arr = [list(map(int, input())) for _ in range(n)]

def sol(x, y, n):
    color = arr[x][y] # 시작점 설정
    # 다른 색상 있는지 확인
    for i in range(x, x+n):
        for j in range(y, y+n):
            # 색상 다르면 4분할로 나눔
            if arr[i][j] != color:
                # 다른 색상 발견하면 ()로 감싸기
                print("(", end="")
                sol(x, y, n//2)
                sol(x, y + n//2, n//2)
                sol(x + n//2, y, n//2)
                sol(x + n//2, y + n//2, n//2)
                print(")", end="")
                return
    # 모든 영역 같은 색상일 때 출력
    print(0 if arr[i][j] == 0 else 1, end="")

sol(0, 0, n)