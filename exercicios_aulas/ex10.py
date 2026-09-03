""" 
Faça uma lista de compras com listas.
O usuário deve ter a possibilidade de inserir, apagar e listar os valores da sua lista
Não permita que o programa quebre com erros de índices inexistentes na sua lista
"""
lista_compras =[]

while True: 
  opcao = input('Selecione uma opção abaixo: [I]nserir [A]pagar [L]istar \n ')
  
  if opcao == 'i':
    opcao_inserir = input('Informe o item que deseja adicionar: ')
    lista_compras.append(opcao_inserir)
    for indice, nome in enumerate (lista_compras):
      print(f'{indice} - {nome}')
    print(f'{opcao_inserir} foi adicionado!')
  
  elif opcao == 'a':
    for indice, nome in enumerate(lista_compras):
      print(f'{indice} - {nome}')
    opcao_apagar = int(input('Informe o número do item que você deseja apagar: '))
    print('Itens das lista de compras: ')
    item_removido = lista_compras.pop(opcao_apagar)
    print(f'{item_removido} foi removido!')
 
  if opcao == 'l':
    print('Itens das lista de compras: ')
    for indice, nome in enumerate(lista_compras):
      print(f'{indice} - {nome}')
   
  # resolver os indices que estão sendo apagados 

