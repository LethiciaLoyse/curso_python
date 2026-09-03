# sistema de segurança simples
senha = input('Por favor, informe a senha: ')
chave_mestra  = input('Você tem a chave mestra? (sim/não?):')
admin = input('É o administrador?')

if senha == '1234' or (chave_mestra == 'sim' or admin == 'sim'):
    print('Acesso autorizado') 
else:
    print('Você não possui acesso')