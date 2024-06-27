# Questão 30
def atualizaMatriz(matriz, lin, col, tipo):
    matriz[lin][col] = tipo
    return matriz

def imprimeJogo(matriz):
    for i in range(3):
        for j in range(3):
            print(matriz[i][j], end="")
        print("")

def jogoTerminou(matriz):
    # Verificar Linhas
    for linha in matriz:
        if linha[0] == linha[1] and linha[1] == linha[2] and linha[0] != ' - ':
            return 1
    
    # Verificar colunas
    for i in range(3):
        if matriz[0][i] == matriz[1][i] and matriz[1][i] == matriz[2][i] and matriz[0][i] != ' - ':
            return 1
        
    # Verificar diagonais
    if matriz[0][0] == matriz[1][1] and matriz[1][1] == matriz[2][2] and matriz[0][0] != ' - ':
        return 1
    
    elif matriz[0][2] == matriz[1][1] and matriz[1][1] == matriz[2][0] and matriz[0][2] != ' - ':
        return 1
    
    # Verificar empate / inacabado
    for linha in matriz:
        if ' - ' in linha:
            return 0
    else:
        return 2
    
matriz = [[' - ', ' - ', ' - '],
          [' - ', ' - ', ' - '],
          [' - ', ' - ', ' - ']]

tipo = ' X '
for i in range(9):
    imprimeJogo(matriz)

    lin, col = input("").split(sep=" ")
    lin, col = int(lin), int(col)

    atualizaMatriz(matriz, lin, col, tipo)

    if i > 2:
        state = jogoTerminou(matriz)
        if state == 1:
            imprimeJogo(matriz)
            print("Ganhou")
            break
        elif state == 2:
            imprimeJogo(matriz)
            print("Empate")
            break

    if tipo == ' X ':
        tipo = ' O '
    else:
        tipo = ' X '