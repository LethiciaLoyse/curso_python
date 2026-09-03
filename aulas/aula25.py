#introdução ao try/except
# isdigit é uma função onde vc consegue ver se o usuario digitou apenas números
# selecionar a variavel e apertar f2, vc consegue renomear. 

# erros são execeções 
# str com sinal de * repete ele 
# if/ else vc checa a condição e muda o fluxo. 
# mas se tiver um erro, o programa para(estoura a exceção) antes de executar o if. 
numero_str = input("Digite um número para dobra-lo:")
try:
    print("STR", numero_str)
    numero_float = float(numero_str)
    print("FLOAT", numero_float )
    print(f"O dobro de {numero_str} é {numero_float * 2:.2f}")
except:
     print("isso não é um número.")

# if numero_str.isdigit():   
# else:
   