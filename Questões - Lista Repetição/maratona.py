# Questão 21
V = int(input())
tempos_lista = list(map(int,input().split()))
tempo_max = max(tempos_lista)
diff = [tempo_max - tempo for tempo in tempos_lista]

print(*diff)