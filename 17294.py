#17294 귀여운 수

k = list(map(int, input()))
k_len = len(k)
res = True
if k_len >= 3 :
    check = k[0] - k[1]
    for i in range(1, k_len - 1) :
        if (k[i] - k[i + 1] != check) :
            res = False
            break
if res == True :
    print('◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!')
else :
    print('흥칫뿡!! <(￣ ﹌ ￣)>')