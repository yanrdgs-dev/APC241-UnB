conj = list(map(int, input().split()))
media_conj = sum(conj) / len(conj)

soma = 0
i = 1
for i in range(len(conj)):
    soma += (conj[i] - media_conj) ** 2

desvio_padrao = (soma / len(conj)) ** 0.5
variancia = desvio_padrao ** 2

print(f'{variancia:.1f}')
print(f'{desvio_padrao:.1f}')