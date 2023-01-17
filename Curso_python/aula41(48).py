"""
*Listas em python
*Alterando uma lista com índices 

tipo list - mutável

suporta vários valores em qualquer tipo

conhecimentos reutilizaveis - indices e fatiamento

metodos uteis: 
append, insert, pop, del, clear, extend, +

append - adiciona um item no final 
insert - adiciona um item no indice escolhido
pop - remove do final ou do indice escolhido
del - apaga um indice
clear - limpa a lista 
extend - estende a lista
+ - -concatena a lista

create, read, update, delete
criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#-----------------Alterando lista em python-----------------------
# 01234
#-54321
# string = "ABCDE" # 5 caracteres

#criando uma lista
# print(lista, type(lista))
# print(bool([])) #falsy

#........0.....1......2.......3....4
#........-5....-4.....-3.....-2...-1
# lista = [123, True, 'Lucas', 1.5, []]
# lista[-3] = "Maria"
# print(lista)
# print(lista[2])

#a lista é interessante remover/adicionar itens no final dela
#pois não requer muito processamento, caso a lista for muito grande

# lista = [10, 20, 30, 40]
# print(lista)
# del lista[2]
# print(lista[1])
# lista.append(50) #adiciona elemento ao final da lista
# lista.pop() #remove elemento ao final da lista
# ultimo_valor = lista.pop()
# print(lista, 'ultimo valor removido', ultimo_valor

#-----------------Alterando lista com incides-----------------------
#        0    1   2   3
# lista = [10, 20, 30, 40]
#        -4   -3  -2   -1
# lista.append('Lucas')
# nome = lista.pop()
# lista.append(123)
# del lista[-1]
# lista.clear()
# lista.insert(0, 5)
# print(lista)

#----------------Concatenando listas em python-----------------------

# lista_a = [1, 2, 3]
# lista_b = [4, 5, 6]
# lista_c = lista_a + lista_b
# print(lista_c)
# lista_a.extend(lista_b)
# print(lista_a)
#quando há espera de retorno de valor de um método
#é usado a variavel acompanhada do método para fazer a modificação

#--------------------dados mutáveis----------------------------

"""
cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""

lista_a = ['Lucas', 'Maria']
lista_b = lista_a.copy()

lista_a[0] = "Qualquer pessoa"
print(lista_b)
print(lista_a)
#exemplo de valor mutável
 



