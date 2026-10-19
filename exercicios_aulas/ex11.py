''' 
Aula 50 - Algoritmo do cpf
'''
cpf = '99213530048'

nove_digitos = cpf[0:9]
regressao = 10


resultado = 0

for digito in nove_digitos:
  resultado += int(digito) * regressao
  regressao -= 1

digito = ((resultado * 10) % 11)

if digito <= 9:
  print(digito)
else:
  ...

