# a, b = 1, 2
# a , b = b , a
# print(a , b)

pessoa = {
    'nome': 'Pedro',
    'sobrenome': 'Cassiano',
}

dados_pessoa = {
    'idade': 17,
    'altura': 1.6
}

dados_completos = {
    **pessoa,
    **dados_pessoa
}

# a, b, c, d = dados_completos.items()
# print(a, b, c, d, sep='\n')

def mostrar_argumentos(*args , **kwargs):

    print('Não nomeados',args)

    for chave, valor in kwargs.items():
        print(chave, valor)

mostrar_argumentos(**dados_completos)