# Questão 26
x = list(map(int, input().split()))
x.pop((len(x) - 1))
x.reverse()
print(*x)