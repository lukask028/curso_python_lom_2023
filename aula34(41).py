"""
while/else
"""

string = 'valor qualquer'

i = 0

while i < len(string):
    letra = string[i]
    
    if letra == ' ':
        break
    print(letra)
    i += 1
    
    
else:
    print("O else foi executado")
    
print("fora do while")

"""
quando o bloco while é executado por completo
ao final é executado o else
"""