maxNum = 0
row, col = 0, 0

for i in range(9):
    arr = list(map(int, input().split()))
    if max(arr) > maxNum:
        maxNum = max(arr)
        row = i
        col = arr.index(maxNum)

print(maxNum)
print(row+1, col+1)
        