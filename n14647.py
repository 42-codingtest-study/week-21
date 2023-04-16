#
# 14647
# 준오는 조류혐오야!!
# https://www.acmicpc.net/problem/14647

n, m = map(int, input().split(' '))
bingo = [0] * n
cnt9_1 = []
cnt9_2 = []

for i in range(n):
    bingo[i] = list(input().split())

# 빙고판 행 확인
for i in bingo:
    cnt = 0
    for j in i:
        if '9' in j:
            cnt += j.count('9')
    cnt9_1.append(cnt)

# 빙고판 열 확인
for i in range(len(bingo[0])):
    cnt = 0
    for j in bingo:
        if '9' in j[i]:
            cnt += j[i].count('9')
    cnt9_2.append(cnt)

if max(cnt9_1) > max(cnt9_2):
    print(sum(cnt9_1) - max(cnt9_1))
else:
    print(sum(cnt9_2) - max(cnt9_2))