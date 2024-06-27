# Questão 5
k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())

qtd = 0

for i in range(1, d+1):
        if not i % k or not i % l or not i % m or not i % n:
                qtd += 1
print(qtd)