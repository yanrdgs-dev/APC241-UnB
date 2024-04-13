l = input().split(":")

h = int(l[0]) * 3600
m = int(l[1]) * 60
s = int(l[2])

total = h + m + s

print(f"La se foram {total} segundos que nao voltam mais...")