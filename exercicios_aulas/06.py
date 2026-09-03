#hora ao usúario    
#Correção do professor
entrada = input('Digite a hora em números inteiros: \n')
try:
    hora = int(entrada)

    if hora >= 0 and hora <= 11:
        print('Bom dia!')
    elif hora >= 12 and hora <= 17:
        print('Boa tarde!')
    elif hora >= 18 and hora <= 23:
        print('Boa noite!')
    else:
        print('Não reconheço essa hora. ')

except:
    print('Digite apenas números inteiros. ')


#minha tentativa
''' 
horario = int(input('Informe a hora atual: \n'))
hora1 = 0 or 11
hora2 = 12 or 17
hora3 = 18 or 23

if 0 or 11 in hora1:
    print('Bom dia!')
elif 12 or 17 in hora2:
    print('Boa tarde!')
elif 18 or 23 in hora3:
    print('Boa noite!')
else:
    ...
    '''