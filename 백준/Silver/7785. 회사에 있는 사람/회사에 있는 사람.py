n = int(input())
tmp = dict()

for _ in range(n):
    a, b = map(str, input().split())
    
    if b == "enter":
        tmp[a] = b
    else:
        del tmp[a]
        
tmp = sorted(tmp.keys(), reverse=True)

for i in tmp:
    print(i)