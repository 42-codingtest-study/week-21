#
# 23321
# 홍익 댄스파티
# https://www.acmicpc.net/problem/23321

arr = [0] * 5
ready = ['.', 'o', 'm', 'l', 'n']
jump = ['o', 'w', 'l', 'n', '.']

for k in range(5):
    arr[k] = list(input())

for i in range (0, len(arr[0])) :
    if arr[1][i] == 'o':
        for j in range (0, 5):
            arr[j][i] = jump[j]
    elif arr[1][i] == 'w':
        for j in range (0, 5):
            arr[j][i] = ready[j]


print(arr)
