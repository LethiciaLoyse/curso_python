#operador and 
# and - todas as condiçõe precisam ser verdadeiras
# Se tiver qualquer valor falso, a expresssão será inteira naquele valor.
# valores falsy -> (0, 0.0, '', False)
# none -> valor que não existe

entrada = input('[E]ntrar [S]air: ')
senha_usuario = input('Senha: ')
senha_permitida = '12345'
if entrada == 'E' and senha_usuario == senha_permitida:
    print('Entrar')
else:
    print('Sair')

#  avaliação de curto circuito
print(True and False and True)
print(True and 0 and True)