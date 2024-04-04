"""
for in com listas
"""
lista = ['Maria', 'Helena', 'Luiz']
indice = 0
indiceF = -len(lista)

for nome in lista:
    print(indice, nome, indiceF)
    indice += 1
    indiceF += 1