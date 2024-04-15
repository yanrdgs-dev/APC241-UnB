def quantosSemestres(matricula,ano_atual,semestre_atual):
        matricula = str(matricula)
        ano_matricula = int(matricula[:2]) + 2000
        semestre_matricula = int(matricula[3:4])
        sub_ano = ano_atual - ano_matricula

        if semestre_atual == 0: 
            total_semestres = sub_ano * 2 - semestre_matricula
            print(total_semestres)
        else:
            total_semestres = sub_ano * 2 - semestre_matricula + semestre_atual
            print(total_semestres)
