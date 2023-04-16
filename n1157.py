#
# 1157
# 단어 공부
# https://www.acmicpc.net/problem/1157

word = list(input().upper())

if len(word) == 1:
    print(word[0])
    exit()

dic = {}

for i in word:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

key = list(dic.keys())
va = list(dic.values()) #value값만 뽑아내기
re_va = sorted(va, reverse=True)

if re_va[0] == re_va[1]: #빈도수가 동일한 값이 있는 경우
    print('?')
else:
    print(key[va.index(re_va[0])])