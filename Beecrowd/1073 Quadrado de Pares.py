numero = int(input())

i = 1
while i <= numero:
    if i % 2 == 0:
        quadrado = i ** 2
        print(f'{i}^2 = {quadrado}')
    i +=1