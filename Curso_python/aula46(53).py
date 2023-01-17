""" 
enumerate - enumera iteráveis (índices)
"""


# [(0, 'maria')(1, 'helena')(2, 'lucas')(3, 'cecilia')]
lista = ['maria', 'helena', 'lucas']
lista.append('cecilia')

# lista_enumerada = enumerate(lista)
# print(next(lista_enumerada))

# for indice, nome in enumerate(lista):
#     print(indice,nome)

# for item in enumerate(lista):
#     indice, nome = item
#     print(indice, nome)
    
for tupla_enumerada in enumerate(lista):
    print('for da tupla:')
    for valor in tupla_enumerada:
        print(f'\t{valor}')
    
