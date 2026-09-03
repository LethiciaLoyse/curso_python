#in e not in 
# está e não está entre
# strings interáveis = vc navegada item por item 
# 0 1 2 3 4 5
# O t á v i o 
# -6-5-4-3-2-1
#nome = 'Otávio'
#print('z'  in nome)
#print('z' not in nome)
nome = input('digite seu nome:')
encontrar = input('Digite o que quer encontrar:')
if encontrar in nome:
    print(f'{encontrar} está dentro de {nome}')
else:
    print(f'{encontrar} não está em {nome}')

