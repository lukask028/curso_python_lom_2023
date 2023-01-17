"""
For + range

range -> range(start, stop, step)

a funcao range não é dependente do for e vice-versa
"""

# numeros = range(10)
# numeros = range(5,10)
# numeros = range(5,10,2)
# print(numeros)

numeros = range(10, 1, -3)

for numero in numeros:
    print(numero)