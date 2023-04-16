#
# 3060
# 욕심쟁이 돼지
# https://www.acmicpc.net/problem/3060

for _ in range(int(input())):
    n = int(input())
    eat = list(map(int, input().split(' ')))
    total = sum(eat)
    day = 1

    while(total <= n):
        day += 1
        total *= 4

    print(day)