t = int(input())

for i in range(t):
    pwd = input()
    left = []
    right = []
    for i in pwd:
        if i == "-":
            if left:
                left.pop()
        elif i == "<":
            if left:
                right.append(left.pop())
        elif i == ">":
            if right:
                left.append(right.pop())
        else:
            left.append(i)
    
    left.extend(reversed(right))
    print(''.join(left))
            