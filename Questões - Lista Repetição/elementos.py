# Questão 22
elementos = list(map(int,input().split()))

repete = len(elementos) != len(set(elementos))

print(repete)