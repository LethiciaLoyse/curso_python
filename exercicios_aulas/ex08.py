'''
faça um jogo de adivinhação de palavra. 
Se a
'''
import os

tentativas = 0
palavra_secreta = 'python'
letras_acertadas = ''

while True: 

    letra_digitada = input('Digite uma letra: ')
    tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada # Atribuindo valores para cada letra digitada

    palavra_formada = '' # mais um concatenação de str´s
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
           palavra_formada += '*'
    print('palavra_formada', palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('cls') # é um import que limpa o terminal
        print('Você ganhou')
        print(f'A palavra secreta era: {palavra_secreta}')
    print(f'O número de tentativas foi {tentativas}')