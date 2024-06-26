x = 0
vezes = int(input())

for i in range(vezes):
    operacao = list(input())  
    if operacao[0] == "+" or operacao[2] == "+":
        x += 1
    elif operacao[0] == "-" or operacao[2] == "-":
        x -= 1

print(x)
    