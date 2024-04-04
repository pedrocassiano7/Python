# Introdução à função lambda (função anônima de uma linha)
# A função lambda é uma função como qualquer
# outra em Python. Porém, são funções anônimas
# que contém apenas uma linha. Ou seja, tudo
# deve ser contido dentro de uma única
# expressão.

# lista = [5, 4, 8, 10, 18, 12, 16]
# lista.sort()
# print(lista)

lista = [
    {'nome': 'Pedro', 'sobrenome': 'Henrique'},
    {'nome': 'Valdeci', 'sobrenome': 'Cassiano'},
    {'nome': 'Michelle', 'sobrenome': 'Fernandes'},
    {'nome': 'Magda', 'sobrenome': 'Elizeth'},
    {'nome': 'Maria', 'sobrenome': 'Aparecida'},
]

def exibir(lista):
    for iten in lista:
        print(iten)
    print('')

l1 = sorted(lista, key=lambda item: item['nome'])
l2 = sorted(lista, key=lambda item: item['sobrenome'])

exibir(l1)
exibir(l2)

