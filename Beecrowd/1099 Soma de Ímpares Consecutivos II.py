x = int(input())
y = int(input())

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