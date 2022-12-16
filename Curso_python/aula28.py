"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""

nome = input(' Digite o seu nome: ')
idade = input(' Digite sua idade: ')
letra = input(' Digite uma letra que queira buscar no nome:')


if nome or idade:
    print('Seu nome é: ' f'{nome}' )
    print(nome[::-1])

if ' ' in nome:
    print(f'O nome: {nome}, contém espaços')
else:
    print(f'seu nome: {nome}, não contém espaços')
if letra in nome:
    print(f'seu nome: {nome} contem a letra: {letra}')
else:
    print(f'seu nome {nome}, não contém a letra: {letra}')
    print(f'seu contem {len(nome)} letras')
    print(f'A primeira letra do seu nome é:  {nome[0]}')
    print(f'A ultima letra do seu nome é: {nome[-1]}')
#nao terminado

