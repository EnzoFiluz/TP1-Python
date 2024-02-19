#7
###Faça um programa que calcule o Índice de Massa Corporal (IMC) do usuário e forneça feedback com base no valor (por exemplo, abaixo do peso, peso normal, sobrepeso).

try:
    peso = float(input("Digite seu peso em quilogramas: "))
    altura = float(input("Digite sua altura em metros: "))

    if peso <= 0 or altura <= 0:
        print("Por favor, digite valores válidos para peso e altura.")
    else:
        altura_squ = altura ** 2
        imc = peso / altura_squ
        imc_round = round(imc, 2)  

        if 18.5 <= imc_round <= 25:
            print(f"Seu peso está dentro da faixa considerada adequada com um IMC de {imc_round}. O IMC recomendado é 18.5 à 25.0. \nContinue mantendo hábitos saudáveis!")
        elif 25 < imc_round <= 30:
            print(f"Você está com sobrepeso com o seu IMC de {imc_round}. O IMC recomendado é 18.5 à 25.0. Recomendamos a adoção de hábitos mais saudáveis para melhorar sua condição.")
        elif imc_round > 30:
            print(f"Seu IMC indica que você está classificado como obeso com um valor de {imc_round}. O IMC recomendado é 18.5 à 25.0. Recomendamos procurar orientação médica para melhor gerenciar sua saúde.")
        else:
            print(f"Seu IMC indica que você está abaixo do peso adequado com um valor de {imc_round}. O IMC recomendado é 18.5 à 25.0. Recomendamos procurar orientação médica para melhorar sua nutrição.")

except ValueError: 
    print("Por favor, insira valores numéricos válidos para peso e altura.")
