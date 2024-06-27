# Questão 20
V = int(input())
tempos_lista = list(map(int,input().split()))
tempo_min = min(tempos_lista)
diff = [tempo - tempo_min for tempo in tempos_lista]

print(*diff)