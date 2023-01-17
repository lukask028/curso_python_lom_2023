#Desempacotamento em chamdas
#de métodos e funções

string = 'abcd'
lista = ['maria', 'helena', 'eduarda']
tupla = 'python', 'é', 'legal'

salas = [
    #0         1
    ['Maria', 'Helena',], #0
    #0
    ['Elaine',], #1
    #0         1         2
    ['Luiz', 'João', 'Eduarda', (0, 10, 20, 30, 40)], #2
]


# a, b, c = lista
# print(a, c)

# p, b, *_, ap, u = lista
# print(p, u, ap)

# * da espaços nas palavras 
# print('maria', 'helena', 1, 2, 3, 'eduarda')
# print(*lista)
# print(*string)
print(*salas)