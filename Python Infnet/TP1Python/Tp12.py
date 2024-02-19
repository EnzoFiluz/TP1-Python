#12
#Crie um programa que classifique as palavras inseridas pelo usuário como curtas (menos de 5 letras) ou longas (5 letras ou mais).

words_user = input("Digite alguma coisa ;)")
quant_pal =len(words_user)

if quant_pal <= 5 : 
    print ("Palavrinha")
    
elif quant_pal > 5 :
    print ("Palavrão")