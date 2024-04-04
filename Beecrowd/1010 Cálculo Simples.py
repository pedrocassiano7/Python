codigoPeca1, qtdPeca1, valorPeca1 = input().split()
codigoPeca1 = int(codigoPeca1)
qtdPeca1 = int(qtdPeca1)
valorPeca1 = float(valorPeca1)

codigoPeca2, qtdPeca2, valorPeca2 = input().split()
codigoPeca2 = int(codigoPeca2)
qtdPeca2 = int(qtdPeca2)
valorPeca2 = float(valorPeca2)

total = qtdPeca1 * valorPeca1 + qtdPeca2 * valorPeca2

print(f'VALOR A PAGAR: R$ {total:.2f}')