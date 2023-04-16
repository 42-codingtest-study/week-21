#
# 2075
# N번째 큰 수
# https://www.acmicpc.net/problem/2075

n = int(input())
all = []

for _ in range(n):
    num = map(int, input().split())

    for i in num:
        all.append(i)

    all.sort(reverse=True)

    if len(all) > n:
        del all[n:]

print(all[n - 1])