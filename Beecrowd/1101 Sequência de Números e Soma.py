while True:
    soma = 0
    m, n = input().split()
    m = int(m)
    n = int(n)

    lista = [m, n]
    organizar = sorted(lista)

    menor = organizar[0]
    maior = organizar[1]

    if n == 0 or m == 0:
        break
    else:
        while menor <= maior:
            soma += menor
            print(menor, end=' ')
            menor += 1
        print(f'Sum={soma}')