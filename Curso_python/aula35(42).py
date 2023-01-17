frase = 'O python é uma linguagem de programação' \
    'multiprograma' \
    'python foi criado por Guido van Rossum.'
    
i = 0
qtd_x_mais_aparece = 0
letra_x_mais_aparece = ''

while i < len(frase):
    letra_atual = frase[i]
    
    if letra_atual == ' ':
        i += 1 
        continue
    
    qtd_x_letra_atual = frase.count(letra_atual)
    
    if qtd_x_mais_aparece < qtd_x_letra_atual:  
        qtd_x_mais_aparece = qtd_x_letra_atual
        letra_x_mais_aparece = letra_atual
        
    i += 1
          
print("a letra que mais apareceu: "
      f'"{letra_x_mais_aparece}" apareceu '
      f'{qtd_x_mais_aparece}x')
    