# Questão 23
qtd_jogadores = int(input())
habilidade_jogadores = list(map(int, input().split()))
habilidade_jogadores.sort(reverse=True)

time_principal = sum(habilidade_jogadores[:11])
time_paia = sum(habilidade_jogadores[11:22])
print(time_principal - time_paia)