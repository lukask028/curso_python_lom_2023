"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import os

palavra_secreta = 'solo'

comp_palavra_secreta = len(palavra_secreta)*'*'
letra_acertada = ''

chance = 0

print(f'{comp_palavra_secreta}')

while True:
    
    letra = input('digite uma letra: ')
    chance += 1

    if len(letra) > 1: 
        print("digite apenas um caractere")
        continue
 
    if letra in palavra_secreta:
        letra_acertada += letra
        print(f'a {letra=} está na palavra {comp_palavra_secreta}')
        
    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letra_acertada:
            
            palavra_formada += letra_secreta
        else:
            # print(f'A {letra=} não está na palavra secreta')
            # print(f'A {comp_palavra_secreta}') 
            palavra_formada += '*'
    
    print('palavra formada:',palavra_formada) 
    
    if palavra_formada == palavra_secreta:
        os.system('cls')
        print("Você completou a palavra! ")
        print("A palavra era: ", palavra_secreta)
        print("Você acertou em " f'{chance} chances')
        letra_acertada = ''
        chance = 0
        
            