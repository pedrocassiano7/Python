# def duplicar(numero):
#     return numero * 2

# def triplicar(numero):
#     return numero * 3

# def quadruplicar(numero):
#     return numero * 4

# print(quadruplicar(2), duplicar(2), triplicar(2))

def multiplicador(multiplicador):
    def multiplicar(numero):
        return multiplicador * numero
    return multiplicar

duplicar = multiplicador(2)
triplicar = multiplicador(3)
quadruplicar = multiplicador(4)

print(duplicar(5))
print(triplicar(5))
print(quadruplicar(5))
