#
# 12866
# 피노키오
# https://www.acmicpc.net/problem/12866

import sys
input = sys.stdin.readline

n = int(input())
chrom = list(input())

cnta = 0
cntc = 0
cntg = 0
cntt = 0

for i in chrom:
    if i == 'A':
        cnta += 1
    elif i == 'C':
        cntc += 1
    elif i == 'G':
        cntg += 1
    elif i == 'T':
        cntt += 1

pino = cnta * cntc * cntg * cntt % 1000000007
print(pino)