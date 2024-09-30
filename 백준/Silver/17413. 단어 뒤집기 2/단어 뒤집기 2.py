# 문자열 스택에 추가
# 괄호 안의 문자는 스택 첫번째부터 pop
# 괄호 외의 문자는 스택 마지막부터 pop
# > 이면 그전까지의 문자 그대로 출력
# 최초의 < 아닌 두번째 이상의 < 이면 그전까지의 문자열 반대로 출력
# 괄호 밖 공백이면 이전 문자열 뒤집고 공백 추가
# 괄호 안의 공백이면 그대로

s = input()
tmp = [] # 임시 저장
res = [] # 최종 문자열 저장
check = False # 괄호 안인지 체크

for i in s:
    if i == ">": # 괄호 끝남
        tmp.append(">")
        res.append(''.join(tmp)) # 괄호 안은 문자열 뒤집지 않음
        tmp = [] # 임시 배열 초기화
    elif i == "<" and tmp: # 최초의 괄호 시작이 아니면
        tmp.reverse() # 문자열 뒤집어서 저장
        res.append(''.join(tmp))
        tmp = [i] # "<"는 임시 배열에 저장해둠
    elif i == " " and "<" not in tmp: # 괄호 밖 공백
        tmp.reverse()
        res.append(''.join(tmp))
        res.append(' ') # 공백 추가해주기
        tmp = []
    else:
        tmp.append(i)
    
# 임시 배열에 문자열 남아있으면 뒤집어서 저장
if tmp:
    tmp.reverse()
    res.append(''.join(tmp))
    
print(''.join(res))
