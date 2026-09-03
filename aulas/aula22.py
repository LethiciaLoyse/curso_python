# interpolação básica de strings 
# s - string
# d e i - int 
# f - float
# x e X - Hexadecimal

nome = 'Luiz'
preco = 100.636363
variavel = '%s, o preço é R$%.2f' % (nome,preco)
print(variavel)
print('O hexadecimal de %d é %06x' % (1500, 1500))