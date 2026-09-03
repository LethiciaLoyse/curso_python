#função input 
#input não salva dados na memória, mas coleta dados de uma variavel. Retorna str´s
#nome = input('Digite seu nome: ')
#print(f'O nome do usuáio é {nome}')
#print(f'O nome do usuáio é {nome=}') --> Esse = mostra o valor da variavel 

numero_1 = int(input('Digite um número: ')) 
numero_2 = int(input('Digite outro número: '))
# Esse tipo de conversão de tipos no incio pode gerar transtornos futuros, 
# caso o usuário digite algo que não seja do tipo inteiro. 
print(f'A soma dos números é: {numero_1 + numero_2}') 
#Aqui ele concatena os valores sem a conversão, 
#pois continuam como str´s




