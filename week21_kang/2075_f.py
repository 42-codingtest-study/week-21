# n번쨰 큰 수
# 메모리초과뜸
n = int(input())

arr = [[0 for _ in range(n)] for _ in range (n)]
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        arr[i][j] = row[j]

check_i = -1
check_j = -1
for k in range(0, n):     
	answer = 0
	for i in range(0, n):
		for j in range(0, n):
			if answer <= arr[i][j]:
				answer = arr[i][j]
				check_i = i
				check_j = j
	arr[check_i][check_j] = 0

print(answer)