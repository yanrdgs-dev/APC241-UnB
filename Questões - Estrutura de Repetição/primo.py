num = int(input())
l = [num]
for i in range(num-1):
    if num % (i+1) == 0:
        l.append(i+1)
l.sort()

if num == 1:
    print("regular")
elif l[0] == 1 and l[1] == num:
    print("primo")
else:
    print("regular")