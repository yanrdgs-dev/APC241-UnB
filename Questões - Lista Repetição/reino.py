# Questão 9
cidadaos = int(input())
qtd = 0
for _ in range(cidadaos):
        n = int(input())
        if n < 1000:
                qtd += 1000 - n
print(qtd)