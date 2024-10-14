T = int(input())
for i in range(T):
  res = []
  ga = input()
  for j in ga:
    if j == '(':
      res.append(j)
    else: # pop을 하는데 스택이 비면 no 출력
      if res: # 비지 않으면
        res.pop()
      else:
        print('NO')
        break
  else: # for-else문 : for문이 break로 끊기지 않았을때 실행
    if not res: # pop에 끊기지 않고 스택이 비면 yes 출력
      print('YES')
    else:
      print('NO')