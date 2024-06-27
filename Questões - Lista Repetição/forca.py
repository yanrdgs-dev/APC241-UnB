'''Cada posição da lista desenho representa um dos estados da forca'''
desenhos = ['''
 +---+
 |   |
     |
     |
     |
     |
========''', '''
 +---+
 |   |
 O   |
     |
     |
     |
========''', '''
 +---+
 |   |
 O   |
 |   |
     |
     |
========''', '''
 +---+
 |   |
 O   |
/|   |
     |
     |
========''', '''
 +---+
 |   |
 O   |
/|\  |
     |
     |
========''', '''
 +---+
 |   |
 O   |
/|\  |
/    |
     |
========''', '''
 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
========'''] 
total_erros = 0
resposta = input("Digite a palavra secreta: ")
print(desenhos[0])
palavra_secreta = ['_'] * len(resposta)

def imprimir_palavra_secreta():
     print()
     for i in palavra_secreta[:-1]:
          print(i, end=" ")
     print(palavra_secreta[-1])

imprimir_palavra_secreta()
while total_erros < 6:  
     tentativa = input("Digite uma letra: ")
     if tentativa in resposta:
          for i in range(len(resposta)):
               if(tentativa == resposta[i]):
                    palavra_secreta[i] = tentativa
          print(desenhos[total_erros])
          imprimir_palavra_secreta()
          
     else:
          total_erros += 1
          print(desenhos[total_erros])
          imprimir_palavra_secreta()
     if palavra_secreta == list(resposta):
          print(f'Sim! A palavra secreta eh "{resposta}"')
          break
     
if total_erros == 6:
     print("Voce teve muitas oportunidades e perdeu!")