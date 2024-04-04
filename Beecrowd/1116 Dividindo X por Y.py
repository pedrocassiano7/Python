casos = int(input())

i = 0
while i <= casos:
    x, y = input().split()
    x = int(x)
    y = int(y)

    if y == 0:
        print('divisao impossivel')
    elif x == 0:
        break
    else:
        resultado = 0
        resultado = x / y
        print(resultado)
