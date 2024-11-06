N = int(input())
num = list(map(int, str(N)))
num.sort(reverse = True)
for i in range(len(num)):
  print(num[i], end = '') 