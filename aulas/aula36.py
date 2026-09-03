'''
Introdução ao for 
For -> para 
In -> cada
'''
texto ='python'

novo_texto = ''
for letra in texto: # A variavél letra é aquela que você coloca o valor do texto
    novo_texto += f'*{letra}'
print(novo_texto + '*')
