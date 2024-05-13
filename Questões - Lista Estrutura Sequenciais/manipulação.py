l = input().split()
a = str(l[0])
b = str(l[1])
x = int(l[2])

def concatenar(str1,str2):
    return str1 + str2

def repetir(str1, inteiro):
    return str1 * inteiro

def ambos(str1,str2,inteiro):
    return repetir(concatenar(str1,str2), inteiro)

print(concatenar(a,b))
print(repetir(a,x))
print(ambos(a,b,x))