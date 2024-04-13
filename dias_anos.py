def age(d):
    a = d // 360
    m = (d % 360) // 30
    d = (d % 360) % 30
    print(f"{a} ano(s), {m} mes(es) e {d} dia(s)")
    
l = input().split()

for i in range(3):
    age(int(l[i]))