""" cadastro de produtos"""

lista_produto = []

print('--- Adicionando produto ao estoque da loja --- ')

while True: 
    meu_produto = input('Qual produto você deseja adicionar? ')
    lista_produto.append(meu_produto)

    escolha = input('Deseja adicionar mais algum item na loja? (s/n) ').lower()
    if escolha == 's':
        print('Sim, eu gostaria!')
    else: 
        print('Você escolheu não adicionar mais produtos!')
        print(lista_produto)
        break
