#1-
#Crie um programa que peça ao usuário para inserir dois números e,
#em seguida, calcule e exiba a soma, subtração, multiplicação, divisão e divisão inteira desses números.

num_one = int(input("Por favor insira um número."))
num_two = int(input ("Por favor insira um número."))

result_sum = num_one + num_two
result_sub = num_one - num_two
result_div = num_one / num_two
result_tim = num_one * num_two
all_results = (result_sum, result_sub, result_div, result_tim)


print("O resultado da soma de " + str(num_one) + " e " + str(num_two) + " é " + str(result_sum))
print("O resultado da subtração de " + str(num_one) + " e " + str(num_two) + " é " + str(result_sub))
print("O resultado da divisão de " + str(num_one) + " e " + str(num_two) + " é " + str(result_div))
print("O resultado da multiplicação de " + str(num_one) + " e " + str(num_two) + " é " + str(result_tim))


 
print("Todos os resultados:", all_results)