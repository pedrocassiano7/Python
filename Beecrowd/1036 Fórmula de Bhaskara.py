import math

a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)

try:
    triangulo = b ** 2 - (4 * a * c)
    r1 = (-b + (math.sqrt(triangulo)))/(2 * a)
    r2 = (-b - (math.sqrt(triangulo)))/(2 * a)

    print(f'R1 = {r1:.5f}')
    print(f'R2 = {r2:.5f}')
except:
    print('Impossivel calcular')