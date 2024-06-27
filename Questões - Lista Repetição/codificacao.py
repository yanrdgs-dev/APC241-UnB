# Questão 7
n = int(input())
n = str(n)[::-1]
if n[-1] == "-":
    print(- int(n[:-1]))
else:
    print(int(n))