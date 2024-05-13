def geraValor1(entrada):
    return entrada % 100000 // 1000

def geraValor2(entrada):
    return entrada % 1000 // 10

def geraValor3(entrada):
    return entrada % 100000 // 10000

def geraValor4(entrada):
    return entrada % 10000 // 100

def geraValor5(entrada):
    return entrada % 10000 // 10

def geraValor6(entrada):
    return entrada % 10

def geraValor7(entrada):
    return entrada // 100000

def geraValor8(entrada):
    aux2 = geraValor1(entrada)
    if (aux2 > 500):
        aux1 = geraValor6(entrada)
        if (aux1 <= 0):
            aux1 = geraValor7(entrada) % 10
            aux2 += aux1
    return aux2

def processaValor(d):
    if (d >= 0 and d < 10): return d + 28
    if (d >= 10): return d + 60 - 10
    return 28

def processaValor2(d):
    if (d > 12): d = d + 1
    if (d >= 0) and (d < 12): return d + 28
    if (d >= 12): return d + 60 - 10
    return 28

def processaValor3(entrada):
    aux1 = geraValor2(entrada) // 3 + geraValor4(entrada)
    
    if aux1 % 10 == 0: return(aux1)
    elif aux1 % 2 == 0: return(aux1 + 1)
    else:
        if not aux1 % 3: return(aux1 * 2)
        else: return (-2 * aux1)

def processaValor4(n1, n2, n3):
    if n1 <= n2 and n1 <= n3:
        v1 = n1
        if n2 <= n3:
            v2 = n2
        else:
            v2 = n3
    elif n2 <= n1 and n2 <= n3:
        v1 = n2
        if n1 <= n3:
            v2 = n1
        else:
            v2 = n3
    else:
        v1 = n3
        if n1 <= n2:
            v2 = n1
        else:
            v2 = n2
    return int(v2-v1)

# Questão 1:
matricula = int(input())

print("Questão 1")
a = geraValor2(matricula)
b = geraValor4(matricula) * .1
c = geraValor5(matricula)

print(f"{a+7*b/3-(c-2):.1f}")

# Questão 2:
print("Questão 2")
print(geraValor8(matricula))

# Questão 3:
print("Questão 3")
print(processaValor(geraValor1(matricula) + geraValor6(matricula)))

# Questão 4:
print("Questão 4")
print(processaValor3(matricula))

# Questão 5:
print("Questão 5")
a = geraValor1(matricula)
b = geraValor3(matricula)
c = geraValor5(matricula)
r = processaValor4(a, b, c)
print(r)