n = int(input())
word = list(input())
num = '0123456789'
hid_num = ''

for i in word:
    if i in num:
        hid_num += i
    else:
        hid_num += ' '

print(sum(int(x) for x in hid_num.split()))