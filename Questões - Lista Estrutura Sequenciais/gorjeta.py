a = input().split()

p1 = a[0]
p2 = a[1]
p3 = a[2]

v1 = float(p1) * 0.1 + float(p1)
v2 = float(p2) * 0.1 + float(p2)
v3 = float(p3) * 0.1 + float(p3)

vt = v1 + v2 + v3

print(f'{v1:.2f} {v2:.2f} {v3:.2f}')
print(f'{vt:.2f}')