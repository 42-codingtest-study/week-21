#
# 17219
# 비밀번호 찾기
# https://www.acmicpc.net/problem/17219

n, m = map(int, input().split())
security = {}

for _ in range(n):
    site, password = input().split()
    security[site] = password

for _ in range(m):
    print(security[input()])