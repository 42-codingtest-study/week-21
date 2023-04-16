k = int(input())

for i in range(0, k) :
	for _ in range(k - i, 0, -1) :
		print("*", end = '')
	print()
