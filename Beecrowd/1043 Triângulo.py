a, b, c, = input().split()
a = float(a)
b = float(b)
c = float(c)

lista = [a, b, c]
organizar = sorted(lista)

if organizar[2] < organizar[0] + organizar[1]:
    perimetro = a + b + c
    print(f'Perimetro = {perimetro}')
else:
    area = (c / 2) * (a + b)
    print(f'Area = {area}')