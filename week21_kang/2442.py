k = int(input())

for i in range(1, k + 1):
	for _ in range(i, k):
		print(' ', end = '')
	for _ in range(1, 2*i):
		print("*", end = '')
	for _ in range(i, k):
		print('', end = '')
	print()

for i in range (1, k + 1) :
	print(' ' * (k - i) + '*' * (2 * i - 1))
