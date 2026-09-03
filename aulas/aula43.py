""" 
Enumerate -> enumera os iteráveis (índices)

"""
lista = ['Calumbi','Loyse','Helena']
lista.append('Jessica')

# Essa linhda de código não muito necessária, posso fazer direto no for!
#lista_enumerada = enumerate(lista) 

#possa ver os indices com o for!
#   for i in enumerate(lista): -> no momento é o recomendável 
    #   print(i)

# Mas, caso eu não queira usar o for possa fazer assim: 
#lista_enumerada = list(enumerate(lista)) 
#print(lista_enumerada)
#OBS: Eu converti em uma lista ou posso fazer em um tupla.
# pq se eu não fizer isso, não irei ver os índices. Frescura do python!

""" 
Posso fazer tambem assim!
"""
for indice, nome in enumerate(lista):
    print(indice, nome)
