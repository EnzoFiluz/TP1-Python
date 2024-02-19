#11
#Faça um programa que simule o lançamento de um dado. O usuário deve escolher quantos dados jogar e o programa deve exibir os resultados.
import random


quantidade_de_dados = int(input("Quantos dados você gostaria de lançar? "))


resultados = [random.randint(1, 6) for _ in range(quantidade_de_dados)]


print(f"Resultados do lançamento: {resultados}")