# Questão 29
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