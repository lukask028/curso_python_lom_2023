"""
Flag (bandeira) - marcar um local
none = não valor
is e is not = é ou não é (tipo, valor, identidade)
id = identidade
"""

# v1 = 'a' #se valores iguais aponta para o mesmo local na memória
# v2 = 'a'
# print(id(v1))
# print(id(v2))

condicao = True
passou_no_if = None

if condicao:
    passou_no_if = True
    print('faça algo')
else:
        print('não faça algo')

print(passou_no_if, passou_no_if is None)
print(passou_no_if, passou_no_if is not None)