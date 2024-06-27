# Questão 16
total = int(input())
compradas = int(input())
l_compradas = []
l_total = []

for i in range(compradas):
    l_compradas.append(int(input()))
l_compradas.sort()
l_compradas = list(set(l_compradas))

for i in range(1, total+1):
    l_total.append(i)

if l_compradas in l_total:
    x = 0
    print(x)
else:
    [l_total.remove(i) for i in range(total+1) if i in l_compradas]
    if l_total == []:
        l_total = 0
        print(l_total)
    else:
        print(len(l_total))
