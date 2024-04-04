casos = int(input())

c = 1
i = 0
o = 0

while c <= casos:
    numero = int(input())
    if 10 <= numero <= 20:
        i += 1
    else:
        o += 1 
    c += 1

print(i, 'in')
print(o, 'out')