k = int(input())

for i in range (k, 0, -1) :
	print(' ' * (k - i) + '*' * (2 * i - 1))
