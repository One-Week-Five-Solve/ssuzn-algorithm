t = int(input())

for _ in range(t):
    n = int(input())
    arr = []
    for _ in range(n):
        t, i = map(int, input().split())
        arr.append((t, i))

    arr.sort(key=lambda x: x[0]) # 서류 성적 오름차순 정렬
    cnt = 1 # 첫번째는 무조건 통과
    top = arr[0][1]
    for i in range(1, n):
        if top > arr[i][1]:
            cnt += 1
            top = arr[i][1]

    print(cnt)