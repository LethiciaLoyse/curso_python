# usuário nome 

primeiro_nome = input('Digite o seu 1° nome: \n')
nome = len(primeiro_nome)

if nome  <= 4:
    print('Seu nome é curto.')
elif nome >= 5 and nome <= 6:      
    print('Seu nome é normal.')
else:   
    print('Seu nome é muito grande. ')
 