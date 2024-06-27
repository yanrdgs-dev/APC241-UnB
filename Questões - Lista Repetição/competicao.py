# Questão 4
x = int(input())
y = 0

for i in range(x):
    i = input().split()
    i[0] = int(i[0])
    i[1] = int(i[1])
    i[2] = int(i[2])
    if i[0] + i[1] + i[2] >= 2:
        y += 1
        
print(y)
    