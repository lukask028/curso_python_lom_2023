""" 
Tipo tupla - uma lista imutável

"""

# _, _, nome, *resto =['maria', 'helena', 'lucas']
# print(nome, resto)

#uso da lista sem precisar edita-la pode usar o tuple
#pode usar ou nao parenteses, na lista de objetos *tuple*
nomes = 'maria', 'helena', 'lucas'
nomes = tuple(nomes) #conversao para tuple
nomes = list(nomes) #conversao para lista
print(nomes[2])
print(nomes)