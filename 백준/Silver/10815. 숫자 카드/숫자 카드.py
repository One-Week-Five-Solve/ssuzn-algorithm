import sys
input = sys.stdin.readline
N = int(input())
num1 = set(map(int, input().split()))
  
M = int(input())
num2 = list(map(int, input().split()))
  
for k in num2:  
  if k in num1:
    print(1, end = ' ')
  else:
    print(0, end = ' ')
        