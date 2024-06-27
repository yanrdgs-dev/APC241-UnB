# Questão 8
x, y = input().split()
x, y = int(x), int(y)
if x > y:
        temp = x
        x = y
        y = temp

primos = 0
for i in range(2, x+1):
        if x % i == 0 and y % i == 0:
                print("Nao sao co-primos!")
                break
        elif i == x:
                primos = 1
if primos:
    print("Sao co-primos.")