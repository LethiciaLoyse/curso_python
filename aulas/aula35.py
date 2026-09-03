'''
iterando strings em python
'''
# \ quebra as linhas de codigo 
# count conta as qnt de vezes que algo apareceu 

frase = 'aooo'

# verificar a letra que mais foi repetida dentro da frase 

i = 0
qnt_mais_vezes = 0
letra_apareceu_mais_vezes = ''
while i < len(frase):
    letra_repetida = frase[i]
    quantas_vezes_letra_apareceu_atual = frase.count(letra_repetida)
    if letra_repetida ==  ' ':
        i += 1
        continue

    if qnt_mais_vezes < quantas_vezes_letra_apareceu_atual:
        qnt_mais_vezes = quantas_vezes_letra_apareceu_atual
        letra_apareceu_mais_vezes = letra_repetida
    i += 1
    print('A letra que apareceu mais vezes foi '
          f'{letra_apareceu_mais_vezes} que apareceu '
          f'{qnt_mais_vezes} x '
          )

# iteração é a quantidade de vezes que o loop foi executado 