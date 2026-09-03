'''
while / else
'''
palavra = 'qualquer valor'

i = 0
while i < len(palavra):
    letra = palavra[i]

    if palavra == ' ':
        break
    print(letra)
    i += 1
else:
    print('O else foi executado')
print('Fora do while ')