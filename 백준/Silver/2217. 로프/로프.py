n = int(input())
lst = []

for _ in range(n):
    a = int(input())
    lst.append(a)
    
lst.sort(reverse=True) # 내림차순 정렬
max_weight = lst[0]

for i in range(n):
    if max_weight < lst[i] * (i + 1):
        max_weight = lst[i] * (i + 1)

print(max_weight)