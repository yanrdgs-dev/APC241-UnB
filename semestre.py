# definir função dos semestres
def quantosSemestres(matricula,ano_atual,semestre_atual):
    # transformar int em str
        matricula = str(matricula)
    # ano e semestre da matrícula
        ano_matricula = int(matricula[:2]) + 2000
        semestre_matricula = int(matricula[3:4])
    
    # subtrair ano atual com ano da matrícula
        sub_ano = ano_atual - ano_matricula
        # se semestre atual = 0, (ano atual - ano matricula) * 2
        if semestre_atual == 0: 
            total_semestres = sub_ano * 2 - semestre_matricula
            print(total_semestres)
            
        # se semestre atual = 1, (ano atual - ano matricula) * 2 - semestre matricula + semestre atual
        else:
            total_semestres = sub_ano * 2 - semestre_matricula + semestre_atual
            print(total_semestres)
