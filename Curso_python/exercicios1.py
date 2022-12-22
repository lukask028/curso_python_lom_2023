"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

# a = input('Digite um número inteiro:')


# try:
#     b = a.isdecimal()
#     if b == True:
#         print("O número é inteiro")
     
#         par = (float(a) %2==0)
#     if par :
#         print("O número digitado foi " f'{a}', " é um número par")
#     else:
#         print("O número digitado foi " f'{a}', " é um número impar")

# except: 
#      print("O número não é inteiro")




# par = (float(a) %2==0)
# if par :
#     print("O número digitado foi " f'{a}', " é um número par")
# else:
#     print("O número digitado foi " f'{a}', " é um número impar")


    
"""a = int(input('Digite um número inteiro:'))
tipo = type(a)
par = ((int(a))%2==0)

if tipo != int :
    print("O número que você digitou não é inteiro.")


if par :
    print("O número digitado foi " f'{(a)}', " é um número par")
else:
    print("O número digitado foi " f'{(a)}', " é um número impar")
"""


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
"""horario = input("Digite um horário exato, entre 0hrs e 23hrs :")
        
try :
    hora = int(horario)

    bomdia = hora >= 0 and hora <= 11 
    boatarde = hora >= 12 and hora <= 17
    boanoite = hora >= 18 and hora  <= 23

    if bomdia:
        print("Bom dia" f' {hora} ' "hrs")

    elif boatarde:
        print("Boa tarde" f' {hora} ' "hrs")

    elif boanoite:                
        print("Boa noite" f' {hora} ' "hrs")

    else:
        print("O horário deve ser entre 0, e 23 hrs")

except:
    print("digite um número")"""
# try:
#     bomdia = horario >= 0 and horario <= 11 
#     boatarde = horario >= 12 and horario <= 17
#     boanoite = horario >= 18 and horario <= 23
#     if horario == bomdia:
#          print("Bom dia" f'{horario}')

#     elif horario == boatarde:
#         print("Boa tarde" f'{horario}')

#     elif horario == boanoite:
#         print("Boa noite" f'{horario}')
# except:
#     print("Número não permitido, insira um horario entre 0h e 23h")         



"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

# nome = input("Escreva seu nome:")


# caracteres = len(nome)
# if caracteres <= 4:
#             print("Seu nome possui" f' {caracteres}' ", é curto")
        
# elif caracteres == 5 or caracteres == 6:
#             print("Seu nome possui" f' {caracteres}' ", é normal")
        
# elif caracteres >= 7:
#             print("Seu nome possui" f' {caracteres}' ", é muito grande")

# else:
#             print("Não foi possível contar as letras.")
