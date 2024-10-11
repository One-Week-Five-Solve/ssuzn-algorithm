S = input()
ans = set()

for i in range(len(S)):
  for j in range(i, len(S)):
    ans.add(S[i:j+1]) # a, ab, abc, b, bc, c
    
print(len(ans))