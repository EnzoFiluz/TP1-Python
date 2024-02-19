#10
#Escreva um programa que combine elementos aleatórios de listas diferentes (personagens, ações, locais) para criar uma história curiosa.
import random

characters = ["Enzo","Jorge","Paula","Joana"]
actions = [" encontrou um tesouro", " perdeu as chaves", " viajou para o espaço", " ganhou na loteria"]
places = [" na praia", " na montanha", " no deserto", " em uma cidade grande"]

characters = random.choice (characters)
actions = random.choice (actions)
places = random.choice (places)

history = f"{characters}{actions}{places}"

print (history)