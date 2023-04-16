#
# 17294
# 귀여운 수~ε٩(๑> ₃ <)۶з
# https://www.acmicpc.net/problem/17294

k = list(map(int, input()))

if len(k) == 1:
    print("◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!")
    exit()

tmp = k[1] - k[0]

for i in range(len(k) - 1):
    if k[i + 1] - k[i] != tmp:
        print("흥칫뿡!! <(￣ ﹌ ￣)>")
        exit()

print("◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!")