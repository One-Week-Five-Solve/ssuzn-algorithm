# 두 원의 접점 개수로 풀이
# 접점 = 0일 때,
# 두개의 원이 만나지 않음, 큰 원 안에 작은 원
# 접점 = 1일 때,
# 외부에서 만날 때, 내부에서 만날 때
# 접접 = 2일 때
# 접점 여러개일 때 (같은 원)
# 중심 사이의 거리 = 루트 (x2-x1)^2 + (y2-y1)^2

import math

t = int(input())
for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = math.sqrt((x2-x1) ** 2 + (y2-y1) ** 2)
    
    if d == 0: # 두 원의 중심 같을 때
        if r1 == r2: # 원이 같은 크기일 때
            print(-1)
        else: # 원이 다른 크기일 때 (큰 원 안에 작은 원)
            print(0)
    else:
        if r1 + r2 > d and abs(r1-r2) < d:
            print(2)
        elif d == r1+r2 or abs(r1-r2) == d:
            print(1)
        else:
            print(0)