''' Calculadora com while '''
# Obs: não se declara variaveis dentro de blocos!

while True:
    num1 = (input('Digite um número: '))
    num2 = (input('Digite outro número: '))
    operador = input('Escolha o operador: (+ - / *)')
    numero_1 = 0
    numero_2 = 0
    numeros_validos = None # <- Checando se foram digitados números. 
    
    try:
        numero_1 = float(num1)
        numero_2 = float(num2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números são inválidos. ')
        continue # se os numeros forem inválidos, eu volto o while.

    # Validando os operadores digitados 
    operadores_digitados = '+-/*'

    if operador not in operadores_digitados:
        print('Operador inválido') # Checando se o usuário digitou o operador certo. 
        continue

    if len(operador) > 1 :
        print('Digite apenas um operador')
        continue
    
    # Operações 
    print('Realizando sua conta. Aguarde o resultado abaixo:')
    if operador == '+':
        print(f'{numero_1} + {numero_2} =', numero_1 + numero_2)
    elif operador == '-':
        print(f'{numero_1} - {numero_2} =', numero_1 - numero_2)
    elif operador == '/':
        print(f'{numero_1} / {numero_2} =', numero_1 / numero_2)
    elif operador == '*':
        print(f'{numero_1} * {numero_2} =', numero_1 * numero_2)
    else:
        print('Se chegou aqui, tem algo errado!')

    sair = input('Deseja continuar? [sim] ou [não]:').lower().startswith('s')
    print(sair)
    if sair is True:
        break