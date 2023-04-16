# 시험 점수
# 두 명의 시험 점수 총합 중 큰 점수 출력

min = sum(map(int, input().split()))
man = sum(map(int, input().split()))

if min > man :
    print (min)
elif min == man :
    print (min)
else :
    print (man)