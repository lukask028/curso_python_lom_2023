"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10
Ex.:  746.824.890-70 (746824890)
   11  10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0 7
   77 40 54 64 14 24 40 36  0 14
Somar todos os resultados: 
70+36+48+56+12+20+32+27+0+14 = 363
Multiplicar o resultado anterior por 10
301 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O primeiro dígito do CPF é 7
"""

import re
import random
import sys
#identando, criando 100 cpf
# for _ in range(100):
nove_digitos = ''
for i in range(9):
    nove_digitos += str(random.randint(0, 9))
print(nove_digitos)


# entrada = input(" cpf [746.824.890-70]: ")
# cpf_enviado_usuario = re.sub(r'[^0-9]',
#                              '',
#                              entrada)
# print(cpf_enviado_usuario)

# entrada_sequencial = entrada == entrada[0] * len(entrada)

# if entrada_sequencial:
#         print('você enviou dados sequencias')
        
        
# nove_digitos = '123123123'
# print(f'{digito_1}')
posicao_numero = 0

multiplicador_regressivo = 10
soma = 0
divisao = 0


if len(nove_digitos) <= 9 :
        print(f'O cpf é {nove_digitos}')
         
    
# posicao dos numeros do cpf:
for digito in nove_digitos[:9]:
        print(f'A posição {posicao_numero} o digito é {digito} \n')
        posicao_numero += 1
# multiplicador dos numeros:
        
        resultado = multiplicador_regressivo * int(digito)
        print(f'Os multiplicadores do digito {digito} x {multiplicador_regressivo} é: {resultado}\n')
        multiplicador_regressivo -= 1
        
# soma dos resultados da multiplicação:
        soma = resultado + soma
        print(f'A soma dos resultados é: {soma}')
        
# resto da divisão da conta anterior:
        digito_1 = (soma * 10) % 11 
        
if digito_1 >= 9 :
        print(f'O resultado é 0 ----- divisao :{digito_1}')

else:
        print(f'O resultado da conta é : {float(digito_1):.3} ')

    
    # -------------------------------------------------------------------
    
dez_digitos = nove_digitos + str(digito_1)
multiplicador_regressivo2 = 11
    
resultado_digito_2 = 0
for digito in dez_digitos:
        # resultado_digito_2 +=  
        resultado_digito_2 += int(digito) * multiplicador_regressivo2
        multiplicador_regressivo2 -= 1
digito_2 = (resultado_digito_2 * 10) % 11
        
digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0
# print(digito_2)
    
cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'
print(cpf_gerado_pelo_calculo)
        
print(cpf_gerado_pelo_calculo)
    