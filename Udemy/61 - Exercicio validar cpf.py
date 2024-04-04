import random

while True:
    cpf = ''
    for numero in range(0, 11):
        cpf += str(random.randint(0, 9))

    nove_digitos = cpf[0:9]
    primeiro_digito = 0
    segundo_digito = 0

    resultado = 0
    contR = 10
    for numero in nove_digitos:
        resultado += int(numero) * contR
        contR -= 1

    resultado *= 10
    resultado %= 11

    if resultado >= 9:
        resultado = 0

    primeiro_digito = str(resultado)

    dez_digitos = nove_digitos + str(resultado)
    resultado = 0
    contR = 11
    for numero in dez_digitos:
        resultado += int(numero) * contR
        contR -= 1

    resultado *= 10
    resultado %= 11

    if resultado >= 9:
        resultado = 0

    segundo_digito = str(resultado)

    if primeiro_digito == cpf[-2] and segundo_digito == cpf[-1]:
        print(f'{cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}')
        break