# Questão 6
n = int(input())

for i in range(1, n + 1):
    if i == 1:
        print(f"{i} elefante incomoda muita gente...")
    else:
        print(f"{i} elefantes incomodam muita gente...")
    print(f"{i+1}" + " elefantes" + " incomodam" + ", incomodam"*(i) + " muito mais...")