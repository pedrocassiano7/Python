funcionario = str(input())
salarioFixo = float(input())
totalVendas = float(input())

total = salarioFixo + (totalVendas * 0.15)

print(f'TOTAL = U$ {total:.2f}')