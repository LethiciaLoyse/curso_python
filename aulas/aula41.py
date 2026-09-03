""" 
Introdução ao desempacotamento + tuplas(tuples)
"""
lista = ['Calumbi','Loyse','Helena'] # é um pacote.
nome1, nome2, nome3 = lista # eu quero extrair determinados dados para colocar em uma variáveis
print(nome2)

"""
OBS: A  qnt de variáveis e de dados da lista precisa ser igual!
Caso contrário, haverá erros 

Suponha que eu quero apenas um valor da lista nomes, o restante dos dados
Devem ser empacotados. É como se eu tivesse outra lista
nome, *resto = lista
(nome1, resto)

Não é legal criar variáveis e não usa-las. Por isso, voce pode usar o underline
Isso mostra que a variável existe, mas eu não vou usar ela agora! 
"""
nome1, *_ = lista
print(nome1, _)