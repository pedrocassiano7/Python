compras = []
import os


while True:
 
    print('[i]nserir [a]pagar [l]istar [e]ncerrar')
    opcao = input('Selecione uma opção: ')
    os.system('cls')


    if opcao == 'i': # opcao inserir
        produto = input('Insira um produto: ')
        compras.append(produto)
    
    if opcao == 'a': # opcao apagar
        d = 0
        for iten in compras:
            print(d, iten)
            d += 1

        try:
            p = int(input('Digite qual opcao deseja apagar: '))
            del compras[p]
        except IndexError:
            print('Indice não existe na lista')
        except ValueError:
            print('Digite um numero inteiro')
    
    if opcao == 'l': # opcao listar
        p = 0
        if len(compras) == 0:
            print('Nada a listar')
        else:
            for iten in compras:
                print(p, iten)
                p += 1
    
    if opcao == 'e': # encerrar
        break