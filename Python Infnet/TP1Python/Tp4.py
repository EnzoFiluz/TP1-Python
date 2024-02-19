###4
###Desenvolva um programa que peça ao usuário para escolher uma operação (adição, subtração, multiplicação, divisão)
###e dois números, e então execute a operação escolhida com os números.

user_choice = input("Escolha uma operação matemática (+,-,/,*) ")
user_num = int(input("Escolha um número "))
user_num2 = int(input("Escolha um número, novamente "))

if user_choice == "+" :
    resultado = user_num + user_num2
    print(f"O resultado da soma é:  {resultado}")
    
elif user_choice == "-" :
    resultado = user_num - user_num2
    print(f"O resultado da subtração é: {resultado}")
    
elif user_choice == "/":
    if user_num2 != 0:  
        resultado = user_num / user_num2
        print(f"Resultado da divisão: {resultado}")
    else:
        print("Não é possível realizar a divisão por zero.")
        
elif user_choice == "*" :
    resultado = user_num * user_num2
    print(f"O resultado da multiplicação é: {resultado}")

