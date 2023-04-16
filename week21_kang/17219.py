#경민아 경민아 비밀번호를 왜 까먹냐
#하나로 통일해라
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
memo = {}
for i in range(n) :
    site, passwd = map(str, input().split())
    memo[site] = passwd

for i in range(m) :
    site = input().rstrip()
    print(memo[site])
