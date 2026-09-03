""" 
Lista de listas e seus índices
"""

salas = [
    # 0         #1 -> aqui são os índices
    ['Maria','Helena'], #0 -> aqui são as listas
    ['Elaine'],#1
    ['Luiz', 'Joao', 'Eduarda', (0,10,20,30,40)] #2
]
print(salas[2][3][3]) # 2= lista, 3 = índice, 3 = índice da tupla

for sala in salas: # Esse for fica com as listas
    print(f'A sala é {sala}')
    for aluno in sala: # Esse fica com os índices
        print(aluno) 