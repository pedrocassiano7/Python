notas = [100, 50, 20, 10, 5, 2, 1]
valor = int(input())

print(valor)
for nota in notas:
    cedula = valor // nota
    print(f'{cedula} nota(s) de R$ {nota},00')
    valor %= nota