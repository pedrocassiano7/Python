a, b, c, = input().split()
a = float(a)
b = float(b)
c = float(c)

lista = [a, b, c]
organizar = sorted(lista)

menor = organizar[0]
meio = organizar[1]
maior = organizar[2]

if maior < meio + menor:
    if (maior ** 2) == (meio ** 2) + (menor ** 2):
        print('TRIANGULO RETANGULO')
    elif (maior ** 2) > (meio ** 2) + (menor ** 2):
        print('TRIANGULO OBTUSANGULO')
    elif (maior ** 2) < (meio ** 2) + (menor ** 2):
        print('TRIANGULO ACUTANGULO')
    if maior == menor == menor:
        print('TRIANGULO EQUILATERO')
    elif maior == menor or maior == meio or meio == menor:
        print('TRIANGULO ISOSCELES')
else:
    print('NAO FORMA TRIANGULO')