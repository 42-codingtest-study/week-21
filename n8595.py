#
# 8595
# 히든 넘버
# https://www.acmicpc.net/problem/8595

n = int(input())
my_string = input()
s = 0
num = ""

for i in range(n):
    if my_string[i].isdigit():
        num += my_string[i]
    else:
        if len(num) != 0:
            s += int(num)
            num = ""
if len(num) != 0:
    s += int(num)

print(s)
