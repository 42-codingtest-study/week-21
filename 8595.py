# n = int(input())
# sen = input()
# hid = ''
# for i in range(n):
#     if (sen[i].isdigit()) == True:
#         hid += sen[i]
#     else:
#         hid += ' '
# # print(hid)  
# res = 0
# find = list(map(str, hid.split(' ')))
# for i in find: 
#     if i != '':
#         res += int(i)
# print(res)

n = int(input())
sen = input()

res = 0
hid = ''
for i in range(n):
    if sen[i].isdigit():
        hid += sen[i]
    else:
        if hid:
            res += int(hid)
            hid = ''

if hid:
    res += int(hid)

print(res)