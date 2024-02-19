#14
#Escreva um programa que permita ao usuário votar em três opções diferentes e, no final, exiba o número de votos de cada opção.

votos_opcao_1 = 0
votos_opcao_2 = 0
votos_opcao_3 = 0

total_votos = int(input("Digite o número total de votos: "))

for voto in range(total_votos):
    print("\nOpções de voto:")
    print("1. Opção 1")
    print("2. Opção 2")
    print("3. Opção 3")

    
    voto_usuario = int(input("Digite o número da sua opção de voto: "))

    
    if voto_usuario == 1:
        votos_opcao_1 += 1
    elif voto_usuario == 2:
        votos_opcao_2 += 1
    elif voto_usuario == 3:
        votos_opcao_3 += 1
    else:
        print("Opção inválida. Voto não contado.")

print("\nResultados dos votos:")
print(f"Opção 1: {votos_opcao_1} votos")
print(f"Opção 2: {votos_opcao_2} votos")
print(f"Opção 3: {votos_opcao_3} votos")
