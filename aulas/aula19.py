#or 
entrada = input('[E]ntrar [S]air: ')
senha_usuario = input('Senha: ')
senha_permitida = '12345'
if (entrada == 'E' or entrada == ('e')) and  senha_usuario == senha_permitida:
    print('Entrar')
else:
    print('Sair')
# qualquer condição verdadeira faz com que toda a condição será verdadeira. 
# print(False or False or False or 'abc') a string é um valor TRUE
# os falsy serão ainda são falsos  
# os parenteses tem a mesma finalidade de prioridade até em condiçoes 

