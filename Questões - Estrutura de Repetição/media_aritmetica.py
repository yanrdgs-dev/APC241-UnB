l = []
i = 0
numero = 0
while numero != (-1):
    numero = (int(input()) ** -1)
    if numero == (-1):
        break
    l.append(numero)
    i += 1
    
soma = sum(l)
media = i // soma
print(f"{media:.0f}")