'''
for + range
range  -> range (star, stop, step)
For e range não dependem uma da outra
criar as variaveis com nomes já definidos, exemplo, range = range ou min = min 
não é recomendavel.
'''
# Um unico valor no range é o stop. exemplos, range(10)
# Em python, o ultimo valor não é incluido
numeros = range(0,100,2) 

for numero in numeros:
    print(numero)

# atenção a steps em númeos negativos! 
numeros = range(0,-100,-1)
for numero in numeros:
    print(numero)