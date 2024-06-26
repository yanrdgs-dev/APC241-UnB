senha = input()

maiuscula = False
minuscula = False
numero = False
simbolo = False
for i in range(len(senha)):
    if senha[i].isupper() == True:
        maiuscula = True
        break
    
for i in range(len(senha)):
    if senha[i].islower() == True:
        minuscula = True
        break

numeros = ["0","1","2","3","4","5","6","7","8","9"]
for i in senha:
    if i in numeros:
        numero = True
        break
    
simbolos = [" ","!","@","#", "$", "%", "^", "&", "*", "(", ")", "-", "+", "?", ",", ".", ";", ":", "'", "}", "{", "/"]

for i in senha:
    if i in simbolos:
        simbolo = True
        break

if maiuscula == True and minuscula == True and numero == True and simbolo == False and len(senha) >= 6 and len(senha) <= 32:
    print("Senha valida.")
else:
    print("Senha invalida.")