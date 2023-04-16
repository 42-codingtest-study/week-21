#
# 2841
# 외계인의 기타연주
# https://www.acmicpc.net/problem/2841

n, p = map(int, input().split())
guitar = [[0] for x in range(7)]
cnt = 0

for _ in range(n):
    line, plat = map(int, input().split())

    while guitar[line][-1] > plat:
        guitar[line].pop()
        cnt += 1

    if guitar[line][-1] == plat:
        continue

    guitar[line].append(plat)
    cnt += 1

print(cnt)