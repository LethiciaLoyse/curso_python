# while + continue 
# o continue faz com que eu consiga pular uma condição dentro do while 
 
contador = 0
 
while contador <= 100:
    contador += 1 # obs: a ordem do print e da soma do contador muda o resultado 

    if contador == 6:
        print('não exibe o !')
        continue

    if contador >= 10 and contador <= 27:
        print(f'não vou mostrar o {contador}')
        continue
    print(contador)
    
    if contador == 40:
        break
