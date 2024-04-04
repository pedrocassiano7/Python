def multiplicar(*args):
    total = 1
    for numero in args:
        total *=numero
    return total

def par_impar(x):
    if x % 2 == 0:
        return f'{x} é Par'
    return f'{x} é Impar'

multiplica1 = multiplicar(5, 2, 5, 2 , 2 ,3)
print(multiplica1)

print(par_impar(4))
print(par_impar(10))
print(par_impar(11))
print(par_impar(9))
    