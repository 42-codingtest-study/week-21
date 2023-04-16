people = []
for _ in range(5):
    people.append(input())
tmp = [''] * 5
mod = []
for i in range(len(people[0])):
    mod = people[0][i] + people[1][i] + people[2][i] + people[3][i] + people[4][i]
    if mod == '.omln':
        tmp[0] += 'o'
        tmp[1] += 'w'
        tmp[2] += 'l'
        tmp[3] += 'n'
        tmp[4] += '.'
    elif mod == 'owln.':
        tmp[0] += '.'
        tmp[1] += 'o'
        tmp[2] += 'm'
        tmp[3] += 'l'
        tmp[4] += 'n'
    elif mod == '..oLn':
        tmp[0] += '.'
        tmp[1] += '.'
        tmp[2] += 'o'
        tmp[3] += 'L'
        tmp[4] += 'n'
    # print("tmp : ",tmp)
        
for draw in tmp:
    print(draw)

# import sys

# people = [list(sys.stdin.readline().rstrip()) for _ in range(5)]
# tmp = ['']*5

# check = {'.omln': ['o', 'w', 'l', 'n', '.'], 'owln.': ['.', 'o', 'm', 'l', 'n'], '..oLn': ['.', '.', 'o', 'L', 'n']}

# for i in range(len(people[0])):
#     mod = people[0][i] + people[1][i] + people[2][i] + people[3][i] + people[4][i]
#     tmp[0] += check[mod][0]
#     tmp[1] += check[mod][1]
#     tmp[2] += check[mod][2]
#     tmp[3] += check[mod][3]
#     tmp[4] += check[mod][4]

# for draw in tmp:
#     print(draw)