###3
#Escreva um programa que receba dois nomes de usuário e os combine de maneira criativa para formar um novo nome.


user_name = input("Bota seu nome ae bro ")
user_lastname = input("Bota seu sobrenome ")

mix_name = user_name[:len(user_name)//2] + user_lastname[ :len(user_lastname)//2]

print (mix_name)