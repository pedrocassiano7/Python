c = 0
soma = 0
for i in range(6):
    numero = float(input())
    if numero > 0:
        c += 1
        soma += numero

media = soma / c
print(f'{c} valores positivos')
print(f'{media:.1f}')