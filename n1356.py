#
# 1356
# 유진수
# https://www.acmicpc.net/problem/1356

n = input()

if len(n) == 1:
    print("NO")
    exit()

for i in range(1, len(n)):
    a = n[:i]
    b = n[i:]

    chka = list(map(int, a)) #a 각 자리수 분리
    chkb = list(map(int, b)) #b 각 자리수 분리

    mula = 1
    mulb = 1

    for i in chka:
        mula *= i

    for i in chkb:
        mulb *= i

    if mula == mulb:
        print("YES")
        exit()

print("NO")