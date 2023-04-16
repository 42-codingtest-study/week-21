#
# 1032
# 명령 프롬프트
# https://www.acmicpc.net/problem/1032

arr = []

for _ in range(int(input())):
    arr.append(list(input()))

result = []

for i in range(len(arr)):
    if i == 0:
        result = arr[i]
    else:
        for j in range(len(result)):
            if result[j] != arr[i][j]:
                result[j] = '?'

print(''.join(result))