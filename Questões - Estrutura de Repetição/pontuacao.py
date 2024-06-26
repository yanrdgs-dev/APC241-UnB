x = list(map(int, input().split()))

menor = min(x)
maior = max(x)
idx_menor = x.index(menor)
idx_maior = x.index(maior)

print(f'{menor} {idx_menor}')
print(f'{maior} {idx_maior}')
print(*x)