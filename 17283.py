import math
l = int(input())
r = int(input())

res = []
while (1):
    l = math.trunc(l * (r/100))
    if l <= 5:
        break;
    # print(l)
    # l = math.trunc(l)
    res.append(l)
sum = 0
n = 2
for i in res:
    sum += (i * n)
    n = n * 2
print(sum)