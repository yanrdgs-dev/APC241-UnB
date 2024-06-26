bill = int(input())
chinelos = list(map(int, input().split()))
chinelos.sort()

for i in range(len(chinelos)):
    if bill <= chinelos[i]:
        print(i)
        quit()
print(-1)