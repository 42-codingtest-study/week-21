k = int(input())

for i in range(0, k):
	for _ in range(0, i):
		print(' ', end = '')
	for _ in range(0, k - i):
		print("*", end = '')
	print()
