# n번째 큰 수
# memory

import heapq
import sys

f = sys.stdin.readline
n = int(f())
total = []
for i in map(int, f().split()):
    heapq.heappush(total, i)

for i in range(1, n):
    a = list(map(int, f().split()))
    for j in range(n):
        if a[j] > total[0]:
            heapq.heappush(total, a[j])
            heapq.heappop(total)
print(total[0])