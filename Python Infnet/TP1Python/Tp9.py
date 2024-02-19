#9
#Desenvolva um programa que aplique descontos diferentes com base no valor da compra:
# desconto de 10% para compras acima de R$100, 15% para compras acima de R$200, etc.

raw_price = float(input("Qual o valor da compra ?"))



if raw_price >= 100 and raw_price < 200:
    desconto = raw_price * 0.10
    total = raw_price - desconto
    print(f"Sua compra de {raw_price} reais, com o desconto de 10% ficou {total} ")
elif raw_price >= 200:
    desconto2 = raw_price * 0.15
    total2 = raw_price - desconto2
    print(f"Sua compra de {raw_price} reais, com o desconto de 15% ficou {total2} ")
else:
    print(f"Sua compra não tem desconto")

