n = int(input())
a = [[0 for _ in range(10)] for _ in range(n+1)]

# 자릿수 1일 때
for i in range(1, 10):
    a[1][i] = 1

# 자릿수 2 이상일 때
for i in range(2, n+1):
    for j in range(10):
        if j == 0:
            a[i][j] = a[i-1][1]
        elif j == 9:
            a[i][j] = a[i-1][8]
        else:
            a[i][j] = a[i-1][j-1] + a[i-1][j+1]

print(sum(a[n]) % 1000000000)