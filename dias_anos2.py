def age(d):
    a = d // 360
    m = (d % 360) // 30
    d = (d % 360) % 30
    print(a, m, d)
    
l = input().split()

for i in range(3):
    age(int(l[i]))