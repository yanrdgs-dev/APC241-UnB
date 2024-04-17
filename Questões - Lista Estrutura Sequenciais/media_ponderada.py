y = input().split()

n1 = float(y[0])
n2 = float(y[1])
n3 = float(y[2])

x = input().split()

p1 = float(x[0])
p2 = float(x[1])
p3 = float(x[2])

somaPeso = p1 + p2 + p3

somaAluno = (n1 * p1) + (n2 * p2) + (n3 * p3)

mediaAluno = somaAluno / somaPeso
print(f'{mediaAluno:.6f}')