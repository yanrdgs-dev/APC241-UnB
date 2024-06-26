datagramas = list(map(int,input().strip().split()))
inversoes = 0

datagramas_certos = sorted(datagramas)
for i in range(len(datagramas)):
    if datagramas_certos[i] != datagramas[i]:
        inversoes += 1
print(inversoes)