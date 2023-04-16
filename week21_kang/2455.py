out_p, in_p = map(int, input().split())
total = 0
answer = 0

while in_p :
    total = total - out_p + in_p
    if total > answer:
        answer = total
    out_p, in_p = map(int, input().split())

print(answer)