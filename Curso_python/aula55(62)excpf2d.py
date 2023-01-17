"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10
Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0
Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O primeiro dígito do CPF é 7
"""
# cpf = 74682489070
cpf = "74682489070"
digito_prova = len(cpf)
digito = int(cpf[0])
# print(f'{digito}')
posicao_numero = 0

multiplicador = 10
soma = 0
divisao = 0
try:

    if digito_prova <= 9 :
         print(f'O cpf é {cpf}')
         print(f'{len(cpf)}')
    
# posicao dos numeros do cpf:
    for digito in cpf[0:10]:
        print(f'A posição {posicao_numero} o digito é {digito} \n')
        posicao_numero += 1
# multiplicador dos numeros:
        numero = int(digito)
        resultado = multiplicador * numero
        print(f'Os multiplicadores do digito {numero} x {multiplicador} é: {resultado}\n')
        multiplicador -= 1
        
# soma dos resultados da multiplicação:
        soma = resultado + soma
        print(f'A soma dos resultados é: {soma}')
        
# resto da divisão da conta anterior:
        divisao = (soma * 10) % 11 
        
    if divisao <= 9 :
        print(f'O resultado da conta é : {float(divisao):.3} ')

    else:
        print(f'O resultado é 0 ----- divisao :{divisao}')
except:
    print("limite de digitos ultrapassados")