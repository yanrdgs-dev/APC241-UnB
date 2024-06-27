# Questão 15
n = int(input())
l = []
for i in range(n):
    l.append(sum(int(x) for x in input().split()))
    j = sum(l)  

if j != 0:
    print("MOVIMENTO")
else:
    print("ESTACIONARIO")