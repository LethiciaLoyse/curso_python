# Número inteiro e par ou ímpar

numero = input("Digite um valor inteiro: ")
resultado = int(numero)


try: 
      if resultado % 2 == 0:
        print(" par ")
      else:
          print("ímpar")
except:
    print("Você não digitou um número inteiro.")
    
# fazendo as correções
# Adiconei o try/ except tbm agora - 13/04 
