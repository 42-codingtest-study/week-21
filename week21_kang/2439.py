k = int(input())

for i in range(1, k + 1):
	for _ in range(0, k - i):
		print(' ', end = '')
	for _ in range(0, i):
		print("*", end = '')
	print()
