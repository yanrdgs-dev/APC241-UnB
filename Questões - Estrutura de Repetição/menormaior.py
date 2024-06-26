n = int(input())
numeros = []
for i in range(n):
    valor = int(input())
    numeros.append(valor)

numeros.sort(reverse=True)
menorValor = numeros[n-1]
maiorValor = numeros[0]

print(f"Menor: {menorValor}")
print(f"Maior: {maiorValor}")