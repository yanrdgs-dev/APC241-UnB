# Questão 2
pa, pb, t1, t2 = input().split()
pa, pb, t1, t2 = int(pa), int(pb), float(t1), float(t2)
t1, t2 = t1/100 + 1, t2/100 + 1

if pa == pb:
    print("Vai alcancar em 0 ano(s).")
elif t1 > t2:
        for i in range(1002):
                if i == 1001:
                        print("Mais de um milenio.")
                pa, pb = int(pa*t1), int(pb*t2)
                if pa >= pb:
                        print(f"Vai alcancar em {i+1} ano(s).")
                        break
else:
        print("A nunca alcancara B.")
