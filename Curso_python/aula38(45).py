"""
iterável -> str, range, etc

iterador -> quem sabe entregar um valor por vez

next -> me entregue o próximo valor

iter -> me entregue o seu iterador
"""

# numeros = range(10)
# numeros = range(5,10)
# numeros = range(5,10,2)
# print(numeros)

# numeros = range(10, 1, -3)

# for numero in numeros:
#     print(numero)

# texto = iter('lucas') #_iter_()
# texto = iter('lucas')

# print(next(texto))
# print(next(texto))
# print(next(texto))
# print(next(texto))
# print(next(texto))
# print(next(texto)) stopiteration msg de erro quando elementos terminam

texto = 'lucas' #iterável
# iterador = iter(texto) #iterator

# while True:
#     try:
#         letra = next(iterador)
#         print(letra)
#     except StopIteration:
#         break

for letra in texto:
    print(letra)