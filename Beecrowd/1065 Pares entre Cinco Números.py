c = 0
for i in range(5):
    numero = float(input())
    if numero % 2 == 0:
        c += 1

print(f'{c} valores pares')