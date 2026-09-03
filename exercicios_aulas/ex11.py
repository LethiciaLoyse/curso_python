''' 
Aula 50 - Algoritmo do cpf
'''
indice = 0
multiplicador = 10

cpf = input('Informe os 9 primeiros digitos dos seu cpf: ')
conversao_cpf = int(cpf)

while cpf > 10:
   print(cpf[indice])
   indice += 1

