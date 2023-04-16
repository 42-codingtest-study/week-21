burger = [int(input()) for i in range(3)]
drink = [int(input()) for i in range(2)]
res = min(burger) + min(drink) - 50
print(res)