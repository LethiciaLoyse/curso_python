'''Iteração com while e strings'''

indice = 0
nome = input('Digite o seu nome: ')
novo_nome = '' # String vazia para acumular valores

while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

print(novo_nome)