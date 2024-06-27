# Questão 12
l = []
i = 0
numero = 0
while numero != (-1):
    numero = int(input())
    if numero == (-1):
        break
    l.append(numero)
    i += 1
    
soma = sum(l)
media = soma // i
print(media)