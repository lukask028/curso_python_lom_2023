""" 
Listas de listas e seus índices
iteráveis dentro de outro iterável 
Tupla dentro de lista
lista dentro de tupla
listra dentro de lista
tupla dentro de tupla
"""

salas = [
    #0         1
    ['Maria', 'Helena',], #0
    #0
    ['Elaine',], #1
    #0         1         2
    ['Luiz', 'João', 'Eduarda', (0, 10, 20, 30, 40)], #2
]

# print(salas[2][3][2])

for sala in salas:
    print(f'A sala é {sala}')
    for aluno in sala:
        print(aluno)


