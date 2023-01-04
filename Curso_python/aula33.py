"""
https://docs.python.org/3/library/stdtypes.html

imutáveis que vimos: str, int, float, bool
"""

string = 'lucas'

# string[3] = 'abc'
print(string[3])

outra_variavel = f'{string[:3]}ABC{string[:4]}'
print(outra_variavel)

print(string.zfill(8))
#zfill ->preenche com zeros a esquerda,
#leva como parametros o total de caracteres escolhido