#13
#Desenvolva um programa que verifique se uma palavra ou frase inserida pelo usuário é um palíndromo (lê-se igual de trás para frente).


entrada_usuario = input("Digite uma palavra ou frase: ")


texto = entrada_usuario.replace(" ", "").lower()


if texto == texto[::-1]:
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")
