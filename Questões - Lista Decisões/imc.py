def ComoVaiSuaSaude(peso, sexo, altura):
    if sexo == "F":
        pesoIdeal = (62.1 * altura) - 44.7
    else:
        pesoIdeal = (72.7 * altura) - 58
    difPeso = peso - pesoIdeal
    x = abs(difPeso)
    imc = peso / (altura ** 2)
    print(x,imc, 0.05 * pesoIdeal)
    # Saúde ótima
    if (18.5 <= imc < 25) and (x <= (0.05 * pesoIdeal)):
        return "Você tem uma saúde ótima!"
    elif (18.5 <= imc < 25) and (x <= (0.1 * pesoIdeal)):
        return "Você tem uma saúde boa."
    elif (18.5 > imc) and (peso < pesoIdeal):
        return "Atenção: Fique atento ao baixo peso!"
    elif (25 <= imc < 30) and (x > (0.1 * pesoIdeal)):
        return "Cuidado: Medidas acima do padrão!"
    elif (imc >= 30) and (x > (0.1 * pesoIdeal)):
        return "Procure ajuda: Excesso de medidas!"
    else:
        return "Sem apontamento."

print(ComoVaiSuaSaude(68,"M", 1.72))
print(ComoVaiSuaSaude(72,"M", 1.92))