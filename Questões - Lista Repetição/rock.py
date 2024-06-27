# Questão 3
pessoas, preco = input().split()
pessoas, preco = int(pessoas), int(preco)

soma = 0
for i in range(pessoas):
        soma += int(input())
        
if soma / pessoas >= preco:
        print(f"media: {int(soma / pessoas)}")
        print("o rock reinara mais uma vez")
else:
        print(f"media: {int(soma / pessoas)}")
        print("rockeiros trabalhando ja")