salario = float(input())
imposto = 0
if 0 <= salario <= 2000:
    print('Isento')

elif 2000 < salario <= 3000:
    imposto = (salario - 2000) * 0.8

elif 3000 < salario <= 4500:
    imposto = (salario - 3000) * 0.18 + (1000 * 0.08)

elif 4500 < salario:
    imposto = (salario - 4500.00) * 0.28 + (1500.00 * 0.18) + (1000.00 * 0.08)

print(f'R$ {imposto:.2f}')
    



