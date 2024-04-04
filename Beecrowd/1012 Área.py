PI = 3.14159
a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)

areaTrianguloR = (a * c)/2
areaCirculo = PI * (c ** 2)
areaTrapezio = ((a + b) * c)/2
areaQuadrado = b ** 2
areaRetangulo = a * b

print(f'TRIANGULO: {areaTrianguloR:.3f}') 
print(f'CIRCULO: {areaCirculo:.3f}')
print(f'TRAPEZIO: {areaTrapezio:.3f}')
print(f'QUADRADO: {areaQuadrado:.3f}')
print(f'RETANGULO: {areaRetangulo:.3f}')
