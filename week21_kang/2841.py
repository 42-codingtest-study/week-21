#외계인의 띵가띵가

count = 0
melody, frets = map(int, input().split())
code = [[0 for _ in range(frets)] for _ in range (6)]

def check_back(m, f):
    check = 0
    global code
    for i in range(f, frets):
        if code[m - 1][i] == 1 :
            code[m - 1][i] == 0
            check += 1
    return check

for _ in range(melody):
    m, f = map(int, input().split())
    a = check_back(m, f)
    print("check_back: ", a)
    print("change_code: ", code)
    if check_back(m, f) :
        count += check_back(m, f)
        print("count111: ", count)
        if code[m - 1][f - 1] == 0 :
            code[m - 1][f - 1] = 1
            count += 1
            print("count222: ", count)
        else :
            continue
            print("count333: ", count)
    else :
        count += 1
        code[m - 1][f - 1] = 1
        print("count444: ", count)

print(count-1)
