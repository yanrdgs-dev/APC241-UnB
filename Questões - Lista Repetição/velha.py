# Questão 28 
def atualizaMatriz(matriz, lin, col, tipo):
    matriz[lin][col] = tipo
    return matriz

def imprimeJogo(matriz):
    for i in range(3):
        for j in range(3):
            print(matriz[i][j], end="")
        print("")