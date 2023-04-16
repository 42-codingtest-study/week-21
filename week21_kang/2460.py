answer = 0
total = 0
for _ in range(10) :
    out_p, in_p = map(int, input().split())
    total = total - out_p + in_p
    if total > answer:
        answer = total

print(answer)