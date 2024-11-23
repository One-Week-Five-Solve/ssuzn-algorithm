n = int(input())

arr = list(map(int, input().split()))
tmp = sorted(set(arr))

dic = {tmp[i]:i for i in range(len(tmp))}

for i in arr:
    print(dic[i], end=' ')
