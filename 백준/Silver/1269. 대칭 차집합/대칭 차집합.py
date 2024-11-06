N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans1 = list(set(A) - set(B))
ans2 = list(set(B) - set(A))

print(len(ans1) + len(ans2))