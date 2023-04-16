import sys
input = sys.stdin.readline

n, m = map(int, input().split())
note = {}

for num in range(n) :
    key, v = input().split()
    note[key] = v
for num2 in range(m) :
    key = input().strip()
    print(note[key])