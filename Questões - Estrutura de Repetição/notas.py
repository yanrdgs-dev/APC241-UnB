total_alunos = int(input())

for i in range(total_alunos):
    nota = list(map(float,input().strip().split()))
    if (sum(nota) / 3) >= 7:
        print(f'O ALUNO {i} FOI APROVADO')
    else:
        print(f'O ALUNO {i} FOI REPROVADO')