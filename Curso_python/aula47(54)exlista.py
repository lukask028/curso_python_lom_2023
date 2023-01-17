""" 
exercicio lista de compras

Faça uma lista de compras com listas
O usuário deve ter a possibilidade de inserir, apagar e listar 
os valores da sua lista
Não permita que o programa quebre com erros de indices inexistentes na lista.
"""
import os

lista_compras = []


while True:
    print("Exiba lista de compras \n Escolha uma opção:")
    resposta = input(" [e]xibir \n [a]pagar \n [i]nserir \n ")
    print('Selecione uma opção')
    

    if resposta == 'i':
        os.system('cls')
        valor = input('Insira um produto: ')
        lista_compras.append(valor)
    elif resposta == 'a':
        indice_str = input(
            'Escolha o índice para apagar: '
        )

        try:
            indice = int(indice_str)
            del lista_compras[indice]
        except ValueError:
            print('Por favor digite número int.')
        except IndexError:
            print('Índice não existe na lista')
        except Exception:
            print('Erro desconhecido')
    elif resposta == 'e':
        os.system('cls')

        if len(lista_compras) == 0:
            print('Nada para listar')

        for i, valor in enumerate(lista_compras):
            print(i, valor)
    else:
        print('Por favor, escolha i, a ou e.')
