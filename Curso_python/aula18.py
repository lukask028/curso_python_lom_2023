#if / elif / else
# se/ se não se / se não
#... ou pass é espaço de código preenchido, para passar, não escrever nada 
#específico naquele momento
#executa apenas uma condição por bloco if / elif 
condicao1 = True
condicao2 = False
condicao3 = False
condicao4 = False


if condicao1:
    print('codigo para condição 1')
elif condicao2: #elif se relaciona a outra condição
   print('codigo para condição 2')
elif condicao3: #elif se relaciona a outra condição
   print('codigo para condição 3')
elif condicao4: #elif se relaciona a outra condição
   print('codigo para condição 4')
else:
    print('todas as condições foram falsas')
#mesmo que haja outras condições verdadeiras nos if, 
#só sera executada a condição verdadeira que o programa
#rodar primeiro
if 10 == 10:
    print('outro if')

    print('fora dos if')