notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]
valor = float(input())

print('NOTAS:')
for nota in notas:
    qtd = valor // nota
    print(f'{qtd:.0f} nota(s) de R$ {nota:.2f}')
    valor %= nota

print('MOEDAS:')
for moeda in moedas:
    qtd = valor // moeda
    print(f'{qtd:.0f} moeda(s) de R$ {moeda:.2f}')
    valor %= moeda