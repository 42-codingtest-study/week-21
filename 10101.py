a = int(input())
b = int(input())
c = int(input())
s = a + b + c
if s != 180:
    print("Error")
elif a == b == c == 60:
    print("Equilateral")
elif a==b or a==c or b==c:
    print("Isosceles")
else:
    print("Scalene")