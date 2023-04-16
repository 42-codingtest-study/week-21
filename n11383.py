#
# 11383
# 뚊
# https://www.acmicpc.net/problem/11383

n, m = map(int, input().split(' '))
original = []
extend = []

for _ in range(n):
    original.append(list(input()))
for _ in range(n):
    extend.append(list(input()))


for i in range(len(original)):
    ori = ''.join(original[i])
    ext = ''.join(extend[i])
    fix = ""
    for j in original[i]:
        fix += j * 2

    if fix != ext:
        print("Not Eyfa")
        exit()

print("Eyfa")