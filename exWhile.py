"""
Iterando strings com while
"""
#       11109876543210
nome = 'Lucas' #iteráveis
#       01234567891011

tamanho_nome = len(nome)
print('nome:', nome)
print('tamanho:', tamanho_nome)
print(nome[4])
posicao_nome = 0


#dicas tamanho da string
#acessar cada indice da string
#while

# while posicao_nome < len(nome):
#     print(nome[0], '*' + nome[1], '*' + nome[2], '*'
#     + nome[3], '*' + nome[4], '*')
    
nova_posicao = ''
while posicao_nome < len(nome):
    letra = nome[posicao_nome]
    nova_posicao += f'*{letra}'
    posicao_nome += 1

nova_posicao += '*'
print(nova_posicao)