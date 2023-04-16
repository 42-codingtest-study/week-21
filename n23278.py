#
# 23278
# 영화 평가
# https://www.acmicpc.net/problem/23278

n, l, h = map(int, input().split())

grade = list(map(int, input().split()))
grade.sort()

for _ in range(l):
    grade.pop(0)

grade.reverse()

for _ in range(h):
    grade.pop(0)

print(sum(grade) / len(grade))
