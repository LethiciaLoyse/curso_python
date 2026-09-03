""" 
Split e join
Split -> Separa as strings
join -> une as strings
obs: retorna uma lista
"""

frase = 'Olha só, que coisa interessante'
lista_frases_cruas = frase.split('a') #Separa a string pelo o que eu colocar dentro do split
# print(lista_frases_cruas)
 
# posso fazer também com listas!

listas_frases = []

for i, frase in enumerate(lista_frases_cruas):
    listas_frases.append(lista_frases_cruas[i].strip())
    # print(lista_frases_cruas)

frases_unidas = ''.join(listas_frases) 
# No join, esse '' é aonde vc está separando. Join(listas_frases) é a lista ou string que vc quer juntar
# Meio estranho pq vc tem que separar primeiro para depois juntar. 
print(frases_unidas)

