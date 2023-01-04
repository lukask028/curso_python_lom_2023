"""Calculadora com while """

while True:
    numero_1 = input('digite um número: ')
    numero_2 = input('digite outro número: ')
    operador = input('digite o operador (+-/*): ')
    
    numeros_validos = None
    
    n1_float = 0
    n2_float = 0
    
    try:
        n1_float = float(numero_1)
        n2_float = float(numero_2)
        numeros_validos = True
    except:
        
        print('error')
        numeros_validos = None
        
        if numeros_validos is None:
            print('Um ou ambos dos números não são válidos')
            continue
        
        
        operadores_permitidos = ('+', '-', '/', '*')
       
        if len(operador) > 1:
           print("Digite apenas um operador")
           continue
       
        if operador not in operadores_permitidos:
           print("Operador inválido")
           continue
       
       
        if operador == '+' :
          
           print(f'{numero_1} + f{numero_2}=', numero_1 + numero_2)
        
        elif operador == '-' :
    
            print(f'{numero_1} - f{numero_2}=', numero_1 - numero_2)
           
        elif operador == '*' :
            print(f'{numero_1} * f{numero_2}=', numero_1 * numero_2)
           
        elif operador == '/' :
            print(f'{numero_1} / f{numero_2}=', numero_1 / numero_2)
           
        else:
            print('operadores inválidos')
       
    sair = input('Quer sair? [s]Sim: ').lower().startswith('s')

    
    if sair is True: 
        break