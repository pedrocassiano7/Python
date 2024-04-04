salario = float(input())

minimo = [0, 400.01, 800.01, 1200.01, 2000.01]
maximo = [400, 800, 1200, 2000, 1000000]
percentual = [15, 12, 10, 7, 4]

p = 0
while p <= 4:
    if minimo[p] <= salario <= maximo[p]:
        reajuste = salario * (percentual[p] / 100)
        total = reajuste + salario
        print(f'Novo salario: {total:.2f}')
        print(f'Reajuste ganho: {reajuste:.2f}')
        print(f'Em percentual: {percentual[p]} %')
    p += 1

