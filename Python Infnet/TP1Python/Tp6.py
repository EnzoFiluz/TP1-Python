#6

import random

random_number = random.randint(1, 10)

tentativas_max = 3

for tentativa_atual in range(1, tentativas_max + 1):
    user_choise = int(input("Digite um número entre 1 e 10"))

    if user_choise == random_number:
        print(f"Acertou mizeravi")
        break
    elif user_choise < random_number:
        print("Tente novamente com um número maior")
    else:
        print("Tente novamente com um número menor")

if tentativa_atual == tentativas_max :
    print(f"Você não conseguiu adivinhar, o numero era {random_number}")