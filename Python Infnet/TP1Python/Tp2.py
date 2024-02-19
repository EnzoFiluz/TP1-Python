###2

### professor, joguei no chatGPT para me ajudar ele so me passava sobre Def, então pesquisei um pouco e usei def.

def minutos_para_horas_e_minutos(total_minutos):
    horas = total_minutos // 60
    minutos = total_minutos % 60
    return horas, minutos

def horas_e_minutos_para_minutos(horas, minutos):
    total_minutos = (horas * 60) + minutos
    return total_minutos


total_minutos_input = int(input("Digite o total de minutos: "))


horas_result, minutos_result = minutos_para_horas_e_minutos(total_minutos_input)
print(f"{total_minutos_input} minutos equivalem a {horas_result} horas e {minutos_result} minutos.")


horas_input = int(input("Digite o número de horas: "))
minutos_input = int(input("Digite o número de minutos: "))

total_minutos_output = horas_e_minutos_para_minutos(horas_input, minutos_input)
print(f"{horas_input} horas e {minutos_input} minutos equivalem a {total_minutos_output} minutos.")











