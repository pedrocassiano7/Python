casos = int(input())

cont = 1
while cont <= casos:
    x, y = input().split()
    x = int(x)
    y = int(y)

    lista = [x, y]
    organizar = sorted(lista)

    x = organizar[0]
    y = organizar[1]

    soma = 0
    x += 1

    while x < y:
        if x % 2 == 1:
            soma += x
        x += 1

    print(soma)

    cont += 1