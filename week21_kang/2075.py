import sys, heapq
input = sys.stdin.readline

n = int(input())
answer = []
for i in range(n):
    num_list = list(map(int, input().split()))
    if not answer:
        for num in num_list :
            heapq.heappush(answer, num)
    else:
        for num in num_list :
            if answer[0] < num :
                heapq.heappush(answer, num)
                heapq.heappop(answer)

print(heapq.heappop(answer))
