n, l, h = map(int, input().split())
score = list(map(int, input().split()))
d = n - l - h
sort_list = sorted(score)
for i in range(l):
    sort_list.pop(0)
for i in range(h):
    sort_list.pop(-1)
sum_list = 0   
for i in range(d):
    sum_list += sort_list[i]

print(sum_list / d)