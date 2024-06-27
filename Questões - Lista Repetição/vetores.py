# Questão 17
dimensao = int(input())
vet1 = list(map(int,input().strip().split()))
vet2 = list(map(int,input().strip().split()))
x = []

for i in range(dimensao):
    x.append(vet1[i] * vet2[i]) 

if sum(x) == 0:
    print("ortogonais")
else:
    print(sum(x))