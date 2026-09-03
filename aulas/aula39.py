'''
Alterando índices em uma lista com del, append e pop
'''

lista = [10,20,30,40]
#numero = lista[2] # estou jogando o valor do item em uma variavel
#del lista[2] deleta o indice solicitado. Python reorganiza os indices
# não é recomendavel fazer com listas muito grandes. 
# O melhor seria alterar o último indice 
lista.append(50)
lista.pop() # ele remove valor e retorna
lista.append(60)
lista.append(70) # append adiciona valores
print(lista) 
